#%%
import numpy as np
from scipy.integrate import odeint
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

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

    for our_value, their_value in zip(our_lst[-1,:], other_lst):
        
        compare_list.append(abs(their_value - our_value) / max([their_value, our_value]))
    
    return compare_list

# Running the simulation
t = np.linspace(0, 80, int(500*24*(24/15)))
results = odeint(adm1_ode, initial_conditions, t, args=(stc_par, bioch_par, phys_par, feed_composition))

# Comparing results and storing in a dictionary
results_compare_list = compare(results, BSM2_results)
results_compare_dict = array_to_dict(results_compare_list)
results_compare_dict

# Putting results into a dataframe
dict_to_df = {
    'Variable': results_compare_dict.keys(),
    'Values': results_compare_dict.values()
}

df_compare = pd.DataFrame(data = dict_to_df)
df_compare['Bins'] = pd.cut(
    df_compare['Values'],
    [10**(-10), 0.0001, 0.001, 0.01, 0.1, 1, 10],
    labels = ['< 0.01%', '0.01 - 0.1%', '0.1 - 1%', '1 - 10%', '10 - 100%', '> 100%']
    )
df_compare


fig = px.bar(
    df_compare.sort_values('Values', ascending=False),
    x='Values',
    y='Variable',
    orientation='h',
    color='Bins'
    )

fig.write_html('results_validation.html')



# %%
