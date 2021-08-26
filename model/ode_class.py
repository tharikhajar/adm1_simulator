# File dedicated for the implementation of the ODE model
#%%
import numpy as np
from importlib import reload
from scipy.integrate import solve_ivp
import pandas as pd

import parameters.parameters_bsm2
reload(parameters.parameters_bsm2)
from parameters.parameters_bsm2 import BSM2_parameters, BSM2_results

import ode
reload(ode)
from ode import adm1_ode


# Eventually, we are going to have more than one substrate
parameters_dict = dict(
    BSM2 = BSM2_parameters
)


class Simulation:
    def __init__(self, substrate="BSM2"):

        self.substrate = substrate

        param = parameters_dict[substrate]

        self.feed_composition_ratios = param['feed_composition_ratios']
        self.initial_condition_ratio = param['initial_condition']['initial_condition_ratio']
        self.pH = param['initial_condition']['pH']
        self.gas_initial_state = param['initial_condition']['gas_initial_state']
        self.stc_par = param['stc_par']
        self.bioch_par = param['bioch_par']
        self.phys_par = param['phys_par']['phys_par']
        self.V_liq = param['phys_par']['V_liq']
        self.V_gas = param['phys_par']['V_gas']
        self.Q_in = param['phys_par']['Q_in']
        self.DQO = param['DQO']
        self.mass = param['mass']
        self.dillution_rate = param['dillution_rate']

        # use for validation
        self.DQO_initial_condition = param['DQO_initial_condition']
        self.BSM2_results = BSM2_results

    def update_parameters(self, DQO, pH, dillution_rate, V_liq, V_gas, mass):
        # Update object based on user input

        self.DQO = DQO
        self.pH = pH
        self.dillution_rate = dillution_rate
        self.V_liq = V_liq
        self.V_gas = V_gas
        self.mass = mass

    def calculate_parameters(self):
        # Update object with parameters in the shape required by ODE function

        self.feed_composition = self.feed_composition_ratios * self.DQO

        initial_condition = self.initial_condition_ratio * self.DQO_initial_condition # Change to DQO after validation
        self.initial_condition = np.concatenate((initial_condition, [np.power(10, -1 * self.pH)], self.gas_initial_state))

        self.Q_in = 170#(self.mass * self.dillution_rate) / 24
        self.phys_par = np.concatenate((self.phys_par, [self.V_liq, self.V_gas, self.Q_in]))

    def simulate(self):
        # Runs the model

        t = np.linspace(0, 300, int(500*24*(24/15)))

        results = solve_ivp(
            adm1_ode, t_span=(t[0], t[-1]),
            y0=self.initial_condition, method='Radau',
            args=(self.stc_par, self.bioch_par, self.phys_par, self.feed_composition),
            rtol=np.power(10., -12),
            atol=np.power(10., -12)
        )

        self.results = results.y
        self.t = results.t
        




#%%
simulate = Simulation('BSM2')
simulate.calculate_parameters()
simulate.simulate()

#%%
simulate.results[:,-1]
