# File dedicated for the implementation of the ODE model
#%%
import parameters.parameters_bsm2 as par
from parameters.parameters_bsm2 import *
import imp
import numpy as np
imp.reload(par)

#%%
# Initial Conditions / Variables

S_su =  0.0124
S_aa =  0.0055
S_fa =  0.1074
S_va =  0.0123
S_bu = 0.0140
S_pro = 0.0176
S_ac =  0.0893
S_h2 =  2.5055*np.power(10, -7)
S_ch4 = 0.0555
S_IC = 0.0951
S_IN = 0.0945
S_I = 0.1309
X_xc = 0.1079
X_ch = 0.0205
X_pr = 0.0842
X_li = 0.0436
X_su = 0.3122
X_aa = 0.9317
X_fa = 0.3384
X_c4 = 0.3258
X_pro = 0.1011
X_ac = 0.6772
X_h2 =  0.2848
X_I =  17.2162
S_cat =  3.5659*np.power(10, -43)
S_an =  0.0052
S_hva = 0.0123  
S_hbu = 0.0140   
S_hpro =  0.0175 
S_hac =  0.0890   
S_hco3 = 0.0857
S_nh3 = 0.0019
S_gas_h2 = 1.1032*np.power(10,-5) 
S_gas_ch4 = 1.6535
S_gas_co2 = 0.0135
Q_D = 178.4674
T_D = 35
S_D1_D = 0
S_D2_D = 0
S_D3_D = 0
X_D4_D = 0
X_D5_D = 0
S_H_ion = 5.4562*np.power(10, -8)

initial_conditions = [
    S_su, #0
    S_aa, #1
    S_fa, #2
    S_va, #3
    S_bu, #4
    S_pro, #5
    S_ac, #6
    S_h2, #7
    S_ch4, #8
    S_IC, #9
    S_IN, #10
    S_I, #11
    X_xc, #12
    X_ch, #13
    X_pr, #14
    X_li, #15
    X_su, #16
    X_aa, #17
    X_fa,#18
    X_c4,#19
    X_pro,#20
    X_ac,#21
    X_h2,#22
    X_I,#23
    S_cat,#24
    S_an,#25
    S_hva,#26
    S_hbu,#27
    S_hpro,#28
    S_hac,#29
    S_hco3,#30
    S_nh3,#31
    S_gas_h2,#32
    S_gas_ch4,#33
    S_gas_co2,#34
    Q_D,#35
    T_D,#36
    S_D1_D, #37
    S_D2_D, #38
    S_D3_D, #39
    X_D4_D, #40
    X_D5_D, #41
    S_H_ion #42
    ] 

#%%
#parametros

# %%
def amd1_ode(initial_conditions, t, stc_par, phys_par, bioch_par):

    S_su, S_fa, S_va, S_bu, S_pro = initial_conditions[0:5]
    S_ac, S_h2, S_ch4, S_IC, S_IN = initial_conditions[5:10]
    S_I, X_xc, X_ch, X_pr, X_li = initial_conditions[10:15]
    X_su, X_aa, X_fa, X_c4, X_pro = initial_conditions[15:20]
    X_pro, X_ac, X_h2, X_I, S_cat = initial_conditions[20:25]
    S_an, S_hva, S_hbu, S_hpro, S_hac = initial_conditions[25:30]
    S_hco3, S_nh3, S_gas_h2, S_gas_ch4, S_gas_co2 = initial_conditions[30:35]
    Q_D, T_D, S_D1_D, S_D2_D, SD3_D = initial_conditions[35:40]
    X_D4_D, X_D5_D, S_H_ion = initial_conditions[40:43]



    
    
