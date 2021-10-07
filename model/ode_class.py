# File dedicated for the implementation of the ODE model
#%%
from os import name
from dash_html_components.Var import Var
import numpy as np
from importlib import reload
from scipy.integrate import solve_ivp
import pandas as pd

# import parameters.parameters_bsm2
# reload(parameters.parameters_bsm2)
# from parameters.parameters_bsm2 import BSM2_parameters, BSM2_results

# import ode
# reload(ode)
# from ode import adm1_ode

import model.parameters.parameters_bsm2
reload(model.parameters.parameters_bsm2)
from model.parameters.parameters_bsm2 import BSM2_parameters, BSM2_results, S_gas_co2, S_gas_h2

import model.ode
reload(model.ode)
from model.ode import adm1_ode

import model.parameters.variables_dictionary
reload(model.parameters.variables_dictionary)
from model.parameters.variables_dictionary import variables_data, Variable


# Eventually, we are going to have more than one substrate
parameters_dict = dict(
    BSM2 = BSM2_parameters
)

class Simulation:
    def __init__(self, substrate="BSM2"):

        self.data = variables_data

        self.substrate = substrate

        param = parameters_dict[substrate]

        self.feed_composition_ratios = param['feed_composition_ratios']
        self.initial_condition_ratio = param['initial_condition']['initial_condition_ratio']
        self.pH = param['initial_condition']['pH']
        self.gas_initial_state = param['initial_condition']['gas_initial_state']
        self.stc_par = param['stc_par']
        self.bioch_par = param['bioch_par']
        self.phys_par_partial = param['phys_par']['phys_par']
        self.V_liq = param['phys_par']['V_liq']
        self.V_gas = param['phys_par']['V_gas']
        self.Q_in = param['phys_par']['Q_in']
        self.DQO = param['DQO']
        self.mass = param['mass']
        self.dillution_rate = param['dillution_rate']
        self.simulation_status = 0

        # use for validation
        self.DQO_initial_condition = param['DQO_initial_condition']
        self.BSM2_results = BSM2_results

    def update_parameters(self, DQO, pH, dillution_rate, V_liq, V_gas, mass):
        ''' Update object based on user input
        '''

        self.DQO = DQO
        self.pH = pH
        self.dillution_rate = dillution_rate
        self.V_liq = V_liq
        self.V_gas = V_gas
        self.mass = mass

    def calculate_parameters(self):
        '''Update object with parameters in the shape required by ODE function
        '''

        self.feed_composition = self.feed_composition_ratios * (self.DQO * (self.mass / self.dillution_rate))

        initial_condition = self.initial_condition_ratio * (self.DQO * (self.mass / self.dillution_rate))
        self.initial_condition = np.concatenate((initial_condition, [np.power(10., -1 * self.pH)], self.gas_initial_state))

        self.Q_in = self.dillution_rate

        self.phys_par = np.concatenate((self.phys_par_partial, [self.V_liq, self.V_gas, self.Q_in]))

    def simulate(self):
        '''Runs the model
        '''

        t = np.linspace(0, 300, int(500*24*(24/15)))

        results = solve_ivp(
            adm1_ode, t_span=(t[0], t[-1]),
            y0=self.initial_condition, method='Radau',
            args=(self.stc_par, self.bioch_par, self.phys_par, self.feed_composition),
            rtol=np.power(10., -12),
            atol=np.power(10., -12)
        )

        # Saving the results in the variables objects
        for variable, result in zip(self.data.keys(), results.y):
            self.data[variable].values = result

        self.t = results.t

        # The gas states are solved in concentration. But we usually want to
        # see it in partial pressure

        R = self.phys_par[0]
        Top = self.phys_par[2]
        gases = ['S_gas_ch4', 'S_gas_co2', 'S_gas_h2']
        gases_denominator = [64, 1, 16]
        for gas, denominator in zip(gases, gases_denominator):
            self.data[gas].values = self.data[gas].values * ((R * Top) / denominator)

        # Creating a pH variable based on H+ concentration
        self.data['pH'] = Variable(
            name='pH',
            unit='',
            vanilla = False,
            ionic = False,
            color='#14213d',
            values = -1 * np.log10(self.data['S_H_ion'].values)
        ) 

    def find_steady_state(self):
        steady_states = []

        for variable in self.data.keys():
            self.data[variable].find_steady_state()
            steady_index = self.data[variable].find_steady_state()
            steady_states.append(steady_index)

        self.steady_state = max(steady_states)

    def calculate_gas_flow_rate(self):

        p_ch4 = self.data['S_gas_ch4'].values
        p_co2 = self.data['S_gas_co2'].values
        p_h2 = self.data['S_gas_h2'].values

        Patm = self.phys_par[16]
        h2o = self.phys_par[17]
        kp = self.phys_par[18]
        h2o_list = []
        q_values = []

        for ch4, co2, h2 in zip(p_ch4, p_co2, p_h2):
            pressure = ch4 + co2 + h2 + h2o
            q_gas = kp * (pressure - Patm)
            # if q_gas < 0: q_gas = 0.
            q_values.append(q_gas)

        q_gas_array = np.array(q_values)

        q_gas_data = Variable(
            name='Vazão de Gás',
            unit='m3 / dia',
            vanilla = False,
            ionic = False,
            color='#14213d',
            values = q_gas_array
        )

        self.data['q_gas'] = q_gas_data

        h2o_array = np.full((len(p_ch4)), h2o)

        h2o_data = Variable(
            name='H2O Gas',
            unit='bar',
            vanilla=False,
            color='#023e8a',
            values=h2o_array,
            category='Fase Gasosa'
        )

        self.data['h2o'] = h2o_data

    def calculate_financial_value(self, energy_price=0.41, generator_efficiency=0.32):
        # Calculates the energy generated (kWh) and the savings (BRL) by month
        # considering the gas flow rate and gas composition at final t

        # Partial Pressures (m-3)
        p_ch4 = self.data['S_gas_ch4'].values[-1]
        p_co2 = self.data['S_gas_co2'].values[-1]
        p_h2 = self.data['S_gas_co2'].values[-1]
        p_h2o = self.phys_par[17]

        ch4_fraction = p_ch4 / (p_ch4 + p_co2 + p_h2 + p_h2o) # fraction of 1

        calorific_value_methane =  9.97 # kWh/m-3
        q_gas = self.data['q_gas'].values[-1] # m-3 / day
        delta_t = 30 # days

        monthly_energy = calorific_value_methane * q_gas * delta_t * ch4_fraction * generator_efficiency
        monthly_savings = monthly_energy * energy_price

        self.monthly_energy = monthly_energy
        self.monthly_savings = monthly_savings


    def set_simulation_status(self, status):
        # Used to determine when the charts can be ploted
        self.simulation_status = status





# %%
