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
#Parameters

# Stoichiometric Parameters

fsI_xc = 0.1
fxI_xc = 0.2
fch_xc = 0.2
fpr_xc = 0.2
fli_xc = 0.3
Nxc = 0.0376/14 # kmole N (kg COD)-1
Ni = 0.06/14 # kmole N (kg COD)-1
Naa = 0.007 # kmole N (kg COD)-1
Cxc = 0.02786 # kmole C (kg COD)-1
CsI = 0.03 # kmole C (kg COD)-1
Cch = 0.0313 # kmole C (kg COD)-1
Cpr = 0.03 # kmole C (kg COD)-1
Cli = 0.022 # kmole C (kg COD)-1
CxI = 0.03 # kmole C (kg COD)-1
Csu = 0.0313 # kmole C (kg COD)-1
Caa = 0.03 # kmole C (kg COD)-1
ffa_li = 0.95
Cfa = 0.0217 # kmole C (kg COD)-1
fh2_su = 0.19
fbu_su = 0.13
fpro_su = 0.27
fac_su = 0.14
Nbac = 0.08/14 # # kmole N (kg COD)-1
Cbu = 0.025 # kmole C (kg COD)-1
Cpro = 0.0268 # kmole C (kg COD)-1
Cac = 0.0313 # kmole C (kg COD)-1
Cbac = 0.0313 # kmole C (kg COD)-1
Ysu = 0.1
fh2_aa = 0.06
fva_aa = 0.23
fbu_aa = 0.26
fpro_aa = 0.05
fac_aa = 0.40
Cva = 0.024 # kmole C (kg COD)-1
Yaa = 0.08
Yfa = 0.06
Yc4 = 0.06
Ypro = 0.04
Cch4 = 0.0156 # kmole C (kg COD)-1
Yac = 0.05
Yh2 = 0.06

stc_par = [
    fsI_xc, #0
    fxI_xc, #1
    fch_xc, #2
    fpr_xc, #3
    fli_xc, #4
    Nxc, #5
    Ni, #6
    Naa, #7
    Cxc, #8
    CsI, #9
    Cch, #10
    Cpr, #11
    Cli, #12
    CxI, #13
    Csu, #14
    Caa, #15
    ffa_li, #16
    Cfa, #17
    fh2_su, #18
    fbu_su, #19
    fpro_su, #20
    fac_su, #21
    Nbac, #22
    Cbu, #23
    Cpro, #24
    Cac, #25
    Cbac, #26
    Ysu, #27
    fh2_aa, #28
    fva_aa, #29
    fbu_aa, #30
    fpro_aa, #31
    fac_aa, #32
    Cva, #33
    Yaa, #34
    Yfa, #35
    Yc4, #36
    Ypro, #37
    Cch, #38
    Yac, #39
    Yh2, #40
]


# Biochemical Parameters
Kdis = 0.5 # d-1
Khyd_ch = 10 # d-1
Khyd_pr = 10 # d-1
Khyd_li = 10 # d-1
Ks_in = np.power(10, -4) # M
Km_su=30 # d-1
Ks_su = 0.5 # kg COD m-3
pHul_aa = 5.5
pHll_aa = 4
km_aa = 50 # d-1
Ks_aa = 0.3 # kg COD m-3
km_fa = 6 # d-1
Ks_fa = 0.4 # kg COD m-3
Kih2_fa = 5 * np.power(10, -6) # kg COD m-3
km_c4 = 20 # d-1
Ks_c4 = 0.2 # kg COD m-3
Kih2_c4 = np.power (10, -5) # kg COD m-3
km_pro = 13 # d-1
Ks_pro = 0.1 # kg COD m-3
Kih2_pro = 3.5*10**(-5) # kg COD m-3
km_ac = 8 # d-1
Ks_ac = 0.15 # kg COD m-3
Ki_nh3 = 0.0018 # M
pHul_ac = 7
pHll_ac = 6
km_h2 = 35 # d-1
Ks_h2 = 7* np.power(10, -6) # kg COD m-3
pHul_h2 = 6
pHll_h2 = 5.0
kdec_Xsu = 0.02 #d-1
kdec_Xaa = 0.02 #d-1
kdec_Xfa = 0.02 #d-1
kdec_Xc4 = 0.02 #d-1
kdec_Xpro = 0.02 #d-1
kdec_Xac = 0.02 #d-1
kdec_Xh2 = 0.02 #d-1

bioch_par = [
    Kdis, #0
    Khyd_ch, #1
    Khyd_pr, #2
    Khyd_li, #3
    Ks_in, #4
    Km_su, #5
    Ks_su, #6
    pHul_aa, #7
    pHll_aa, #8
    km_aa, #9
    Ks_aa, #10
    km_fa, #11
    Ks_fa, #12
    Kih2_fa, #13
    km_c4, #14
    Ks_c4, #15
    Kih2_c4, #16
    km_pro, #17
    Ks_pro, #18
    Kih2_pro, #19
    km_ac, #20
    Ks_ac, #21
    Ki_nh3, #22
    pHul_ac, #23
    pHll_ac, #24
    km_h2, #25
    Ks_h2, #26
    pHul_h2, #27
    pHll_h2, #28
    kdec_Xsu, #29
    kdec_Xaa, #30
    kdec_Xfa, #31
    kdec_Xc4, #32
    kdec_Xpro, #33
    kdec_Xac, #34
    kdec_Xh2, #35
]


# Physiochemical Parameters
r = 0.083145
t_base = 298.15
t_op = 308.15
t_inv_dif = ((1/t_base)-(1/t_op))

R = r # bar M-1 K-1
Tbase = t_base # K
Top = t_op # K
Kw = np.exp((55900/(r*100))*t_inv_dif) # M 10-14
Ka_va = np.power(10, -4.86) # M
Ka_bu = np.power(10, -4.82) # M
Ka_pro = np.power(10, -4.88) # M
Ka_ac = np.power(10, -4.76) # M
Ka_co2 = np.power(10, -6.35)*np.exp((7646/(r*100)*t_inv_dif)) # M
Ka_IN = np.power(10, -9.25)*np.exp((51965/(r*100)*t_inv_dif)) # M
kA_Bva = np.power(10, 10) # M-1 d-1
kA_Bbu = np.power(10, 10) # M-1 d-1
kA_Bpro = np.power(10, 10) # M-1 d-1
kA_Bac = np.power(10, 10) # M-1 d-1
kA_Bco2 = np.power(10, 10) # M-1 d-1
kA_BIN = np.power(10, 10) # M-1 d-1
Patm = 1.013 # bar
pgas_h2o = 0.0313 * np.exp(5290*t_inv_dif) # bar
kp = 5 * np.power(10, 4) # m3 d-1 bar-1
kLa = 200 # d-1
Kh_co2 = 0.035 * np.exp((-19410/(r*100))*t_inv_dif)
Kh_ch4 = 0.0014 * np.exp((-14240/(r*100))*t_inv_dif)
Kh_h2 = (7.8*np.power(10, -4)) * np.exp((-4180/(r*100))*t_inv_dif)
V = 3400 # m3
Qin = 300 # m3 d-1

phys_par = [
    R, #0
    Tbase, #1
    Top, #2
    Kw, #3
    Ka_va, #4
    Ka_bu, #5
    Ka_pro, #6
    Ka_ac, #7
    Ka_co2, #8
    Ka_IN, #9
    kA_Bva, #10
    kA_Bbu, #11
    kA_Bpro, #12
    kA_Bac, #13
    kA_Bco2, #14
    kA_BIN, #15
    Patm, #16
    pgas_h2o, #17
    kp, #18
    kLa, #19
    Kh_co2, #20
    Kh_ch4, #21
    Kh_h2, #22
    V, #23
    Qin, #24
]

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



    
    
