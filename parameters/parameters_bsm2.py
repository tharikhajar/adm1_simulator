# This file holds the parameter set from Rosen; Jeppsson 2006 implementation of ADM1 within the BSM2 framework
# This implementation is intended for urban waste water digestion and is widely used as an implementation validadion
#%%
import numpy as np
#%%
# Stoichiometric Parameter Values
stc_par = {
    'fsI_xc': 0.1,
    'fxI_xc': 0.2,
    'fch_xc': 0.2,
    'fpr_xc': 0.2,
    'fli_xc': 0.3,
    'Nxc': 0.0376/14, # kmole N (kg COD)-1
    'Ni': 0.06/14, # kmole N (kg COD)-1
    'Naa': 0.007, # kmole N (kg COD)-1
    'Cxc': 0.02786, # kmole C (kg COD)-1
    'CsI': 0.03, # kmole C (kg COD)-1
    'Cch': 0.0313, # kmole C (kg COD)-1
    'Cpr': 0.03, # kmole C (kg COD)-1
    'Cli': 0.022, # kmole C (kg COD)-1
    'CxI': 0.03, # kmole C (kg COD)-1
    'Csu': 0.0313, # kmole C (kg COD)-1
    'Caa': 0.03, # kmole C (kg COD)-1
    'ffa_li': 0.95,
    'Cfa': 0.0217, # kmole C (kg COD)-1
    'fh2_su': 0.19,
    'fbu_su': 0.13,
    'fpro_su': 0.27,
    'fac_su': 0.14,
    'Nbac': 0.08/14, # # kmole N (kg COD)-1
    'Cbu': 0.025, # kmole C (kg COD)-1
    'Cpro': 0.0268, # kmole C (kg COD)-1
    'Cac': 0.0313, # kmole C (kg COD)-1
    'Cbac': 0.0313, # kmole C (kg COD)-1
    'Ysu': 0.1,
    'fh2_aa': 0.06,
    'fva_aa': 0.23,
    'fbu_aa': 0.26,
    'fpro_aa': 0.05,
    'fac_aa': 0.40,
    'Cva': 0.024, # kmole C (kg COD)-1
    'Yaa': 0.08,
    'Yfa': 0.06,
    'Yc4': 0.06,
    'Ypro': 0.04,
    'Cch4': 0.0156, # kmole C (kg COD)-1
    'Yac': 0.05,
    'Yh2': 0.06
}

#%%

# Biochemical Parameter Values
bioch_par = {
    'Kdis': 0.5, # d-1
    'Khyd_ch': 10, # d-1
    'Khyd_pr': 10, # d-1
    'Khyd_li': 10, # d-1
    'Ks_in': 1*10**(-4), # M
    'Km_su':30, # d-1
    'Ks_su': 0.5, # kg COD m-3
    'pHul_aa': 5.5,
    'pHll_aa': 4,
    'km_aa': 50, # d-1
    'Ks_aa': 0.3, # kg COD m-3
    'km_fa': 6, # d-1
    'Ks_fa': 0.4, # kg COD m-3
    'Kih2_fa': 5*10**(-6), # kg COD m-3
    'km_c4': 20, # d-1
    'Ks_c4': 0.2, # kg COD m-3
    'Kih2_c4': 10**(-5), # kg COD m-3
    'km_pro': 13, # d-1
    'Ks_pro': 0.1, # kg COD m-3
    'Kih2_pro': 3.5*10**(-5), # kg COD m-3
    'km_ac': 8, # d-1
    'Ks_ac': 0.15, # kg COD m-3
    'Ki_nh3': 0.0018, # M
    'pHul_ac': 7,
    'pHll_ac': 6,
    'km_h2': 35, # d-1
    'Ks_h2': 7*10**(-6), # kg COD m-3
    'pHul_h2': 6,
    'pHll_h2': 5.0,
    'kdec_Xsu': 0.02, #d-1
    'kdec_Xaa': 0.02, #d-1
    'kdec_Xfa': 0.02, #d-1
    'kdec_Xc4': 0.02, #d-1
    'kdec_Xpro': 0.02, #d-1
    'kdec_Xac': 0.02, #d-1
    'kdec_Xh2': 0.02 #d-1
}
# %%

# Physiochemical parameter values
r = 0.083145
t_base = 298.15
t_op = 308.15
t_inv_dif = ((1/t_base)-(1/t_op))

phys_par = {
    'R': r, # bar M-1 K-1
    'Tbase': t_base, # K
    'Top': t_op, # K
    'Kw': np.exp((55900/(r*100))*t_inv_dif), # M 10-14
    'Ka_va': 10**(-4.86), # M
    'Ka_bu': 10**(-4.82), # M
    'Ka_pro': 10**(-4.88), # M
    'Ka_ac': 10**(-4.76), # M
    'Ka_co2': 10**(-6.35)*np.exp(
        (7646/(r*100)*t_inv_dif) # M
    ),
    'Ka_IN': 10**(-9.25)*np.exp(
        (51965/(r*100)*t_inv_dif) # M
    ),
    'kA_Bva': 10**(10), # M-1 d-1
    'kA_Bbu': 10**(10), # M-1 d-1
    'kA_Bpro': 10**(10), # M-1 d-1
    'kA_Bac': 10**(10), # M-1 d-1
    'kA_Bco2': 10**(10), # M-1 d-1
    'kA_BIN': 10**(10), # M-1 d-1
    'Patm': 1.013, # bar
    'pgas_h2o': 0.0313 * np.exp(5290*t_inv_dif), # bar
    'kp': 5*10**(4), # m3 d-1 bar-1
    'kLa': 200, # d-1
    'Kh_co2': 0.035 * np.exp((-19410/(r*100))*t_inv_dif),
    'Kh_ch4': 0.0014 * np.exp((-14240/(r*100))*t_inv_dif),
    'Kh_h2': (7.8*10**(-4)) * np.exp((-4180/(r*100))*t_inv_dif),
    'V': 3400, # m3
    'Qin': 300 # m3 d-1
}
#%%
# Feed composition

feed = {
    'Ssu': 0.01, # kg COD m-3
    'Saa': 0.001, # kg COD m-3
    'Sfa': 0.001, # kg COD m-3
    'Sva': 0.001, # kg COD m-3
    'Sbu': 0.001, # kg COD m-3
    'Spro': 0.001, # kg COD m-3
    'Sac': 0.001, # kg COD m-3
    'Sh2': 10**(-8), # kg COD m-3
    'Sch4': 10**(-5), # kg COD m-3
    'Sic': 0.04, # kmole m-3
    'Sin': 0.01, # kmole m-3
    'Si': 0.02, # kg COD m-3
    'Xxc': 2.0, # kg COD m-3
    'Xch': 5.0, # kg COD m-3
    'Xpr': 20.0, # kg COD m-3
    'Xli': 5.0, # kg COD m-3
    'Xsu': 0.0, # kg COD m-3
    'Xaa': 0.01, # kg COD m-3
    'Xfa': 0.01, # kg COD m-3
    'Xc4': 0.01, # kg COD m-3
    'Xpro': 0.01, # kg COD m-3
    'Xac': 0.01, # kg COD m-3
    'Xh2': 0.01, # kg COD m-3
    'Xi': 25.0, # kg COD m-3
    'Scat': 0.04, # kmole m-3
    'San': 0.02 # kmole m-3
}