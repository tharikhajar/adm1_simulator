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
    y0=initial_conditions,  method='RK45',
    args=(stc_par, bioch_par, phys_par, feed_composition)
)
#%%
# Putting both results in the same shape

results_odeint = np.transpose(results_odeint)
t_ivp = results_ivp_full.t
results_ivp = results_ivp_full.y

#%%

results_ivp_dict = array_to_dict(results_ivp)
results_odeint_dict = array_to_dict(results_odeint)
#%%

df_ivp = pd.DataFrame(data=results_ivp_dict)
df_odeint = pd.DataFrame(data=results_odeint_dict)

df_ivp = pH_post_calculation(df_ivp)
df_odeint = pH_post_calculation(df_odeint)

df_ivp['Time (days)'] = t_ivp
df_odeint['Time (days)'] = t


compare_ivp = compare(df_ivp.tail(1).values[0][:-4], BSM2_results)
compare_odeint = compare(df_odeint.tail(1).values[0][:-4], BSM2_results)

compare_ivp_dict = array_to_dict(compare_ivp)
compare_odeint_dict = array_to_dict(compare_odeint)

df_compare = pd.DataFrame(data={
    'Variables': compare_ivp_dict.keys(),
    'Error (ivp)': compare_ivp_dict.values(),
    'Error (odeint)': compare_odeint_dict.values()
})

df_compare


df_compare
#%%
df_compare['Bins (odeint)'] = pd.cut(
    df_compare['Error (odeint)'],
    [10**(-10), 0.0001, 0.001, 0.01, 0.1, 1, 10],
    labels = ['< 0.01%', '0.01 - 0.1%', '0.1 - 1%', '1 - 10%', '10 - 100%', '> 100%']
    )


#%%
# Plotting a bar chart to visualize the error by variable
fig = px.bar(
    df_compare.sort_values('Error (odeint)', ascending=True),
    x='Error (odeint)',
    y='Variables',
    orientation='h',
    color='Bins (odeint)'
    )

fig.write_html('results_validation.html')


#%%
# Normalizing because couldn't get the y axis to rescale properly to fit every variable

df_results_normalized = pd.DataFrame()

for col in df_results.columns:
    df_results_normalized[col] = df_results[col] / max(df_results[col])

df_results_normalized['Time'] = t
df_results_normalized

#%%
# Animation in plotly works with data in the long version

df_results_molten = pd.melt(
    df_results_normalized, id_vars='Time',
    value_vars=df_results_normalized.columns[:-1],
    var_name='Variable', value_name='Values'
    )


#%%
# Creating and exporting the chart

fig_animated = px.scatter(
    df_results_molten, x='Time',
    y='Values', animation_frame='Variable',
    range_x=[0, max(t)], range_y=[0, 1.1]
)

fig_animated.write_html('timeseries.html')


#
# %%
# pressure post relative chart

df = gas_pressure_post_calculation(df_odeint)

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
    yaxis=dict(
        type='linear',
        range=[1, 100],
        ticksuffix='%'))

fig.write_html('pressure.html')
# %%
# Pressure absolute

fig = go.Figure()

pressure_states = ['Pressure (H2)', 'Pressure (CH4)', 'Pressure (CO2)', 'Pressure (H20)']
pressure_colors = ['#264653', '#2a9d8f', '#f4a261', '#e76f51']

for state, color in zip(pressure_states, pressure_colors):
    fig.add_trace(go.Scatter(
        x=df['Time (days)'], y=df[state],
        mode='lines', stackgroup='one',
        name=state,
        line=dict(
            width=0.5, color=color
        )
    ))

fig.update_layout(
    showlegend=True,
    xaxis_type='category',
)

fig.write_html('pressure_absolute.html')
# %%

# Taking a look at gas flow rate
plt.plot(df['Time (days)'], df['Gas Flow'])
plt.show()
# %%
