#%%
import numpy as np
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

import ode, support_functions, parameters.parameters_bsm2
from importlib import reload
reload(ode)
reload(support_functions)
reload(parameters.parameters_bsm2)

from ode import *
from support_functions import *
from parameters.parameters_bsm2 import BSM2_results

# Defining function to compare simulation results
def compare(our_lst, other_lst):
    
    compare_list = []

    for our_value, their_value in zip(our_lst, other_lst):
        
        compare_list.append(abs(their_value - our_value) / average([their_value, our_value]))
    
    return compare_list

def results_to_df(results, label, t, compare_switch=True):
    '''
    results: 2-dimensional array containing the simulation results
    label: label to identify the simulation (e.g. odeint, ivp)
    t: one dimensional array with the simulation timesteps
    compare: whether to return an additional DataFrame with comparisom with BSM2 results

    returns one or two DataFrames (depending on compare switch) 
    '''

    results_dict = array_to_dict(results)
    df = pd.DataFrame(data=results_dict)
    df = pH_post_calculation(df)
    df = gas_pressure_post_calculation(df)
    df['Time (days)'] = t

    if compare_switch == True:

        import parameters.parameters_bsm2
        from importlib import reload
        reload(parameters.parameters_bsm2)
        from parameters.parameters_bsm2 import BSM2_results

        compare_array = compare(df.tail(1).values[0][:-10], BSM2_results)
        compare_dict = array_to_dict(compare_array)
        df_compare = pd.DataFrame(data={
            'Variables': compare_dict.keys(),
            f'Relative Error ({label})': compare_dict.values()
        })

        df_compare[f'Bins ({label})'] = pd.cut(
            df_compare[f'Relative Error ({label})'],
            [10**(-10), 0.0001, 0.001, 0.01, 0.1, 1, 10],
            labels = ['< 0.01%', '0.01 - 0.1%', '0.1 - 1%', '1 - 10%', '10 - 100%', '> 100%']
            )

        return df, df_compare

    return df

def plot_all_time_series(df, label=''):

    # Normalizing because couldn't get the y axis to rescale properly to fit every variable
    df_normalized = pd.DataFrame()

    for col in df.columns[:-1]:
        df_normalized[col] = df[col] / max(df[col])

    time_column_name = df.columns[-1]

    df_normalized[time_column_name] = df[time_column_name]

    # Animation in plotly express works with data in the long version
    df_results_molten = pd.melt(
        df_normalized, id_vars=time_column_name,
        value_vars=df_normalized.columns[:-1],
        var_name='Variable', value_name='Values'
        )

    fig_animated = px.scatter(
        df_results_molten, x=time_column_name,
        y='Values', animation_frame='Variable',
        range_x=[0, max(t)], range_y=[0, 1.1]
        )

    fig_animated.write_html(f'validation_charts/timeseries_{label}.html')
    return df_normalized, df_results_molten

def plot_compare(df, label=''):

    x_values = df.columns[1]
    y_values = df.columns[0]
    color_values = df.columns[2]

    df['Data Labels'] = (round(df[x_values] * 100, 4)).astype(str) + '%'

    fig = px.bar(
        df.sort_values(x_values, ascending=True),
        x=x_values,
        y=y_values,
        orientation='h',
        color=color_values,
        text='Data Labels'
        )

    fig.write_html(f'validation_charts/results_validation_{label}.html')


def plot_pressure(df, label=''):


    fig = go.Figure()

    pressure_states = ['Pressure (H2)', 'Pressure (CH4)', 'Pressure (CO2)', 'Pressure (H20)']
    pressure_colors = ['#264653', '#2a9d8f', '#f4a261', '#e76f51']

    for state, color in zip(pressure_states, pressure_colors):
        fig.add_trace(go.Scatter(
            x=df['Time (days)'], y=df[state],
            mode='lines', stackgroup='one',
            groupnorm='percent', name=state,
            line=dict(
                width=0.5, color=color
            )
        ))
    fig.update_layout(
        showlegend=True,
        xaxis_type='category',
        xaxis=dict(
          dtick=len(df[df.columns[-1]]) / 10
        ),
        yaxis=dict(
            type='linear',
            range=[1, 100],
            ticksuffix='%')
            )

    fig.write_html(f'validation_charts/pressure_{label}.html')

#%%

# Running the simulation
t = np.linspace(0, 150, int(500*24*(24/15)))
print(t[-1])
results_odeint = odeint(
    adm1_ode, y0=initial_conditions, 
    t=t, tfirst=True,
    args=(stc_par, bioch_par, phys_par, feed_composition)
    )
#%%
results_ivp_full = solve_ivp(
    adm1_ode, t_span=(t[0], t[-1]),
    y0=initial_conditions,  method='Radau',
    args=(stc_par, bioch_par, phys_par, feed_composition),
    rtol=np.power(10., -12),
    atol=np.power(10., -12)
)

#%%
# Run this if you want to analyze ODEINT results
label = 'odeint_fixed_KIH2_pro'
df, df_compare = results_to_df(
    results=np.transpose(results_odeint), 
    label=label, 
    t=t)

#%%
# Run this if you want to analyze IVP results
label = 'ivp_more_decimal_points'
df, df_compare = results_to_df(
    results=results_ivp_full.y, 
    label=label, 
    t=results_ivp_full.t
    )

#%%
# Export charts based on chosen simulation
# Don't forget to add a label in the cell above

plot_compare(df_compare, label=label)
df_norm, df_molten = plot_all_time_series(df, label=label)
plot_pressure(df, label=label)
#%%

results_ivp_full.y

# %%
