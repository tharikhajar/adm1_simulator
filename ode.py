# File dedicated for the implementation of the ODE model
#%%
import numpy as np
from numpy.core.defchararray import array
from numpy.lib.function_base import average
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import pandas as pd

#%%

# Feed Composition

S_su_in = 0.01 # kg COD m-3
S_aa_in = 0.001 # kg COD m-3
S_fa_in = 0.001 # kg COD m-3
S_va_in = 0.001 # kg COD m-3    
S_bu_in = 0.001 # kg COD m-3
S_pro_in = 0.001 # kg COD m-3
S_ac_in = 0.001 # kg COD m-3
S_h2_in = np.power(10., -8.) # kg COD m-3
S_ch4_in = np.power(10., -5.) # kg COD m-3
S_IC_in = 0.04 # kmole m-3
S_IN_in = 0.01 # kmole m-3
S_I_in = 0.02 # kg COD m-3
X_xc_in = 2.0 # kg COD m-3
X_ch_in = 5.0 # kg COD m-3
X_pr_in = 20.0 # kg COD m-3
X_li_in = 5.0 # kg COD m-3
X_su_in = 0.0 # kg COD m-3
X_aa_in = 0.01 # kg COD m-3
X_fa_in = 0.01 # kg COD m-3
X_c4_in = 0.01 # kg COD m-3
X_pro_in = 0.01 # kg COD m-3
X_ac_in = 0.01 # kg COD m-3
X_h2_in = 0.01 # kg COD m-3
X_I_in = 25.0 # kg COD m-3
S_cat_in = 0.04 # kmole m-3
S_an_in = 0.02 # kmole m-3

feed_composition = [ 
    S_su_in, #0
    S_aa_in, #1
    S_fa_in, #2
    S_va_in, #3
    S_bu_in, #4
    S_pro_in, #5
    S_ac_in, #6
    S_h2_in, #7
    S_ch4_in, #8
    S_IC_in, #9
    S_IN_in, #10
    S_I_in, #11
    X_xc_in, #12
    X_ch_in, #13
    X_pr_in, #14
    X_li_in, #15
    X_su_in, #16
    X_aa_in, #17
    X_fa_in, #18
    X_c4_in, #19
    X_pro_in, #20
    X_ac_in, #21
    X_h2_in, #22
    X_I_in, #23
    S_cat_in, #24
    S_an_in #25
]

# Initial Conditions / Variables

S_su =  0.0124
S_aa =  0.0055
S_fa =  0.1074
S_va =  0.0123
S_bu = 0.0140
S_pro = 0.0176
S_ac =  0.0893
S_h2 =  2.5055*np.power(10., -7.)
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
S_cat =  3.5659*np.power(10., -43.)
S_an =  0.0052
S_hva = 0.0123  
S_hbu = 0.0140   
S_hpro =  0.0175 
S_hac =  0.0890   
S_hco3 = 0.0857
S_nh3 = 0.0019
S_gas_h2 = 1.1032*np.power(10.,-5.) 
S_gas_ch4 = 1.6535
S_gas_co2 = 0.0135
Q_D = 178.4674
T_D = 35
S_D1_D = 0
S_D2_D = 0
S_D3_D = 0
X_D4_D = 0
X_D5_D = 0
S_H_ion = 5.4562*np.power(10., -8.)

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
    S_H_ion #35
    ] 


#Parameters

# Stoichiometric Parameters

fsI_xc = 0.1
fxI_xc = 0.2
fch_xc = 0.2
fpr_xc = 0.2
fli_xc = 0.3
Nxc = 0.0376 / 14 # kmole N (kg COD)-1
Ni = 0.06 / 14 # kmole N (kg COD)-1
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
fac_su = 0.41
Nbac = 0.08 / 14 # # kmole N (kg COD)-1
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
Ks_in = np.power(10., -4.) # M
Km_su = 30 # d-1
Ks_su = 0.5 # kg COD m-3
pHul_aa = 5.5
pHll_aa = 4
km_aa = 50 # d-1
Ks_aa = 0.3 # kg COD m-3
km_fa = 6 # d-1
Ks_fa = 0.4 # kg COD m-3
Kih2_fa = 5 * np.power(10.,-6.) # kg COD m-3
km_c4 = 20 # d-1
Ks_c4 = 0.2 # kg COD m-3
Kih2_c4 = np.power(10., -5.) # kg COD m-3
km_pro = 13 # d-1
Ks_pro = 0.1 # kg COD m-3
Kih2_pro = 3.5 * np.power(10., -5.) # kg COD m-3
km_ac = 8 # d-1
Ks_ac = 0.15 # kg COD m-3
Ki_nh3 = 0.0018 # M
pHul_ac = 7
pHll_ac = 6
km_h2 = 35 # d-1
Ks_h2 = 7 * np.power(10., -6.) # kg COD m-3
pHul_h2 = 6
pHll_h2 = 5
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

R = 0.083145 # bar M-1 K-1
Tbase = 298.15 # K
Top = 308.15 # K

t_inv_dif = ((1 / Tbase) - (1 / Top))

Kw = np.power(10., -14.) * np.exp((55900 / (R * 100)) * t_inv_dif) # M 10^-14
Ka_va = np.power(10., -4.86) # M
Ka_bu = np.power(10., -4.82) # M
Ka_pro = np.power(10., -4.88) # M
Ka_ac = np.power(10., -4.76) # M
Ka_co2 = np.power(10., -6.35) * np.exp((7646 / (R * 100)) * t_inv_dif) # M
Ka_IN = np.power(10., -9.25) * np.exp((51965 / (R * 100)) * t_inv_dif) # M
kA_Bva = np.power(10., 10.) # M-1 d-1
kA_Bbu = np.power(10., 10.) # M-1 d-1
kA_Bpro = np.power(10., 10.) # M-1 d-1
kA_Bac = np.power(10., 10.) # M-1 d-1
kA_Bco2 = np.power(10., 10.) # M-1 d-1
kA_BIN = np.power(10., 10.) # M-1 d-1
Patm = 1.013 # bar
pgas_h2o = 0.0313 * np.exp(5290 * t_inv_dif) # bar
kp = 5 * np.power(10., 4.) # m^3 d-1 bar-1
kLa = 200 # d-1
Kh_co2 = 0.035 * np.exp((-19410 / (R * 100)) * t_inv_dif)
Kh_ch4 = 0.0014 * np.exp((-14240/(R * 100)) * t_inv_dif)
Kh_h2 = (7.8 * np.power(10., -4.)) * np.exp((-4180 / (R * 100)) * t_inv_dif)
V_liq = 3400 # m^3
V_gas = 300 # m^3
Q_in = 170 # m^3 d-1


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
    V_liq, #23
    V_gas, #24
    Q_in #25
]

# %%
def adm1_ode(initial_conditions, t, stc_par, bioch_par, phys_par, feed_composition):

    # Feed Composition

    S_su_in, S_aa_in, S_fa_in, S_va_in, S_bu_in = feed_composition[0:5]
    S_pro_in, S_ac_in, S_h2_in, S_ch4_in, S_IC_in = feed_composition[5:10]
    S_IN_in, S_I_in, X_xc_in, X_ch_in, X_pr_in = feed_composition[10:15]
    X_li_in, X_su_in, X_aa_in, X_fa_in, X_c4_in = feed_composition[15:20]
    X_pro_in, X_ac_in, X_h2_in, X_I_in, S_cat_in, S_an_in = feed_composition[20:]

    # Variables

    S_su, S_aa, S_fa, S_va, S_bu, S_pro = initial_conditions[0:6] #faltou o S_aa #1
    S_ac, S_h2, S_ch4, S_IC, S_IN = initial_conditions[6:11]
    S_I, X_xc, X_ch, X_pr, X_li = initial_conditions[11:16]
    X_su, X_aa, X_fa, X_c4, X_pro = initial_conditions[16:21]
    X_ac, X_h2, X_I, S_cat, S_an = initial_conditions[21:26]
    S_hva, S_hbu, S_hpro, S_hac, S_hco3 = initial_conditions[26:31]
    S_nh3, S_gas_h2, S_gas_ch4, S_gas_co2, S_H_ion = initial_conditions[31:]

    # Stoichimetric Parameters
    
    fsI_xc, fxI_xc, fch_xc, fpr_xc, fli_xc = stc_par[0:5]
    Nxc, Ni, Naa, Cxc, CsI = stc_par[5:10]
    Cch, Cpr, Cli, CxI, Csu = stc_par[10:15]
    Caa, ffa_li, Cfa, fh2_su, fbu_su = stc_par[15:20]
    fpro_su, fac_su, Nbac, Cbu, Cpro = stc_par[20:25]
    Cac, Cbac, Ysu, fh2_aa, fva_aa = stc_par[25:30]
    fbu_aa, fpro_aa, fac_aa, Cva, Yaa = stc_par[30:35]
    Yfa, Yc4, Ypro, Cch, Yac = stc_par[35:40]
    yh2 = stc_par[40] 


    # Biochemical Parameters

    Kdis, Khyd_ch, Khyd_pr, Khyd_li, Ks_in = bioch_par[0:5]
    Km_su, Ks_su, pHul_aa, pHll_aa, km_aa = bioch_par[5:10]
    Ks_aa, Km_fa, Ks_fa, Kih2_fa, km_c4 = bioch_par[10:15]
    Ks_c4, Kih2_c4, km_pro, Ks_pro, Kih2_pro = bioch_par[15:20]
    km_ac, Ks_ac, Ki_nh3, pHul_ac, pHll_ac = bioch_par[20:25]
    km_h2, Ks_h2, pHul_h2, pHll_h2, kdec_Xsu = bioch_par[25:30]
    kdec_Xaa, kdec_Xfa, kdec_Xc4, kdec_Xpro, kdec_Xac = bioch_par[30:35]
    kdec_Xh2 = bioch_par[35]
    
    # Physical Parameters
    
    R, Tbase, Top, Kw, Ka_va = phys_par[0:5]
    Ka_bu, Ka_pro, Ka_ac, Ka_co2, Ka_IN = phys_par[5:10]
    kA_Bva, kA_Bbu, kA_Bpro, kA_Bac, kA_Bco2 = phys_par[10:15]
    kA_BIN, Patm, pgas_h2o, kp, kLa = phys_par[15:20]
    Kh_co2, Kh_ch4, Kh_h2, V_liq, V_gas, Q_in = phys_par[20:]

    # pH Inhibition

    S_nh4 = S_IN - S_nh3
    S_co2 = S_IC - S_hco3
    theta = S_cat + S_nh4 - S_hco3 - (S_hac / 64) - (S_hpro / 112) - (S_hbu / 160) - (S_hva / 208) - S_an
    
    S_H_ion = -1 * (theta / 2.) + (.5 * np.power(np.power(theta, 2.) + 4. * Kw, .5))
    
    pH = -1 * np.log10(S_H_ion)
    # pH = -1 * np.log10(S_H_ion)

    # Hill inhibition function based on hydrogen ions

    Kph_aa = np.power(10., -((pHll_aa + pHul_aa) / 2.))
    Kph_ac = np.power(10., -((pHll_ac + pHul_ac) / 2.))
    Kph_h2 = np.power(10., -((pHll_h2 + pHul_h2) / 2.))
    
    n_aa = 3. / (pHul_aa - pHll_aa) 
    n_ac = 3. / (pHul_ac - pHll_ac)
    n_h2 = 3. / (pHul_h2 - pHll_h2)

    pH_n_aa = np.power(pH, n_aa)
    I_pH_aa = pH_n_aa / (pH_n_aa + np.power(Kph_aa, n_aa))
    pH_n_ac = np.power(pH, n_ac)
    I_pH_ac = pH_n_ac / (pH_n_ac + np.power(Kph_ac, n_ac))
    pH_n_h2 = np.power(pH, n_h2)
    I_pH_h2 = pH_n_h2 / (pH_n_h2 + np.power(Kph_h2, n_h2))

    I_IN_lim = 1. / (1 + (Ks_in / S_IN))
    I_h2_fa = 1. / (1 + (S_h2 / Kih2_fa))
    I_h2_c4 = 1. / (1 + (S_h2 / Kih2_c4))
    I_h2_pro = 1. / (1 + (S_h2 / Kih2_pro))
    I_nh3 = 1. / (1 + (S_nh3 / Ki_nh3))
    
    I5 = I6 = I_pH_aa * I_IN_lim
    I7 = I_pH_aa * I_IN_lim * I_h2_fa
    I8 = I9 = I_pH_aa * I_IN_lim * I_h2_c4
    I10 = I_pH_aa * I_IN_lim * I_h2_pro
    I11 = I_pH_ac * I_IN_lim * I_nh3
    I12 = I_pH_h2 * I_IN_lim
    

    # Biochemical process rates 

    rho1 = Kdis * X_xc # Particulate matter disintegration
    rho2 = Khyd_ch * X_ch # Carbohydrate Hydrolyzation
    rho3 = Khyd_pr * X_pr # Prtotein Hydrolyzation
    rho4 = Khyd_li * X_li # Lipids Hydrolyzation
    rho5 = Km_su * (S_su / (Ks_su + S_su)) * X_su * I5 # 
    rho6 = km_aa * (S_aa / (Ks_aa + S_aa)) * X_aa * I6 #
    rho7 = km_fa * (S_fa / (Ks_fa + S_fa)) * X_fa * I7 #
    rho8 = km_c4 * (S_va / (Ks_c4 + S_va)) * X_c4 * (S_va / (S_bu + S_va + np.power(10.,-6.))) * I8 #
    rho9 = km_c4 * (S_bu / (Ks_c4 + S_bu)) * X_c4 * (S_bu / (S_bu + S_va + np.power(10.,-6.))) * I9 #
    rho10 = km_pro * (S_pro / (Ks_pro + S_pro)) * X_pro * I10 #
    rho11 = km_ac * (S_ac / (Ks_ac + S_ac)) * X_ac * I11 #
    rho12 = km_h2 * (S_h2 / (Ks_h2 + S_h2)) * X_h2 * I12 # 
    rho13 = kdec_Xsu * X_su # Decay of micoorganisms consumers of monosaccharides 
    rho14 = kdec_Xaa * X_aa # Decay of micoorganisms consumers of aminoacids
    rho15 = kdec_Xfa * X_fa # Decay of micoorganisms consumers of fat acids
    rho16 = kdec_Xc4 * X_c4 # Decay of micoorganisms consumers of valeric and butiric acids
    rho17 = kdec_Xpro * X_pro # Decay of micoorganisms consumers of propionic acid
    rho18 = kdec_Xac * X_ac # Decay of micoorganisms consumers of acetic acid
    rho19 = kdec_Xh2 * X_h2 # Decay of micoorganisms consumers of hydrogen




    # Acid-base rates  CHECK DOCUMENT ION SIGNALS ON EQUATIONS
    
    rho_a4 = kA_Bva * ( S_hva * (Ka_va + S_H_ion) - Ka_va * S_va) # for Valeric Acid
    rho_a5 = kA_Bbu * ( S_hbu * (Ka_bu + S_H_ion) - Ka_bu * S_bu) # for Butiric Acid
    rho_a6 = kA_Bpro * ( S_hpro * (Ka_pro + S_H_ion) - Ka_pro * S_pro) # for Propionic Acid
    rho_a7 = kA_Bac * ( S_hac * (Ka_ac + S_H_ion) - Ka_ac * S_ac) # for Acetic Acid
    rho_a10 = kA_Bco2 * ( S_hco3 * (Ka_co2 + S_H_ion) - Ka_co2 * S_IC) # for Carbonic Acid and Dissolved CO2 (related) [is hco3 already hco3-?]
    rho_a11 = kA_BIN * ( S_nh3 * (Ka_IN + S_H_ion) - Ka_IN * S_IN) # for Ammonia


    # Gas transfer rates
    
    pgas_h2 = S_gas_h2 * ((R * Top) / 16) # used in rho_T_8
    pgas_ch4 = S_gas_ch4 * ((R * Top) / 64) # used in rho_T_9
    pgas_co2 = S_gas_co2 * R * Top # used in rho_T_10
    # S_co2 = S_IC - S_hco3 # Moved to the top so that it happens before pH calculation
    
    rho_T_8 = kLa * (S_h2 - 16 * Kh_h2 * pgas_h2)
    rho_T_9 = kLa * (S_ch4 - 64 * Kh_ch4 * pgas_ch4)
    rho_T_10 = kLa * (S_co2 - Kh_co2 * pgas_co2)


    Pgas = pgas_h2 + pgas_ch4 + pgas_co2 + pgas_h2o # to calculate the qgas

    qgas = kp * (Pgas - Patm) * (Pgas / Patm)

    
    
    # Differential Equations Implementation
    
    # Water Phase Equations
    # Soluble Matter

    QV_ratio = (Q_in/V_liq)
    
    dt_S_su = QV_ratio * (S_su_in - S_su) + rho2 + (1 - ffa_li) * rho4 - rho5 # 1 
    dt_S_aa = QV_ratio * (S_aa_in - S_aa) + rho3 - rho6 #2
    dt_S_fa = QV_ratio * (S_fa_in - S_fa) + (ffa_li * rho4) - rho7 #3
    dt_S_va = QV_ratio * (S_va_in - S_va) + (1 - Yaa) * fva_aa * rho6 - rho8 #4
    dt_S_bu = QV_ratio * (S_bu_in - S_bu) + (1 - Ysu) * fbu_su * rho5 + (1 - Yaa) * fbu_aa * rho6 - rho9 #5
    dt_S_pro = QV_ratio * (S_pro_in - S_pro) + (1 - Ysu) * fpro_su * rho5 + (1-Yaa) * fpro_aa * rho6 + (1-Yc4) * 0.54 * rho8 - rho10 #6
    dt_S_ac = QV_ratio * (S_ac_in - S_ac) + (1 - Ysu) * fac_su * rho5 + (1-Yaa) * fac_aa * rho6 + (1-Yfa) * 0.7 * rho7 + (1-Yc4) * 0.31 * rho8 + (1-Yc4) * 0.8 * rho9 + (1-Ypro) * 0.57 * rho10 - rho11 #7 
    dt_S_h2 = QV_ratio * (S_h2_in - S_h2) + (1 - Ysu) * fh2_su * rho5 + (1-Yaa) * fh2_aa * rho6 + (1-Yfa) * 0.3 * rho7 + (1-Yc4) * 0.15 * rho8 + (1-Yc4) * 0.2 * rho9 + (1-Ypro) * 0.43 * rho10 - rho12 - rho_T_8 #8
    dt_S_ch4 = QV_ratio * (S_ch4_in - S_ch4) + (1-Yac) * rho11 + (1-Yh2) * rho12 - rho_T_9 #9
    
    # Sum for equation 10
    # s equations

    s1 = (- Cxc) + (fsI_xc * CsI) + (fch_xc * Cch) + (fpr_xc * Cpr) + (fli_xc * Cli) + (fxI_xc * CxI)
    s2 = (- Cch) + Csu
    s3 = (- Cpr) + Caa
    s4 = (- Cli) + ((1 - ffa_li) * Csu) + (ffa_li * Cfa)
    s5 = (- Csu) + ((1 - Ysu) * ((fbu_su * Cbu) + (fpro_su * Cpro) + (fac_su * Cac))) + (Ysu * Cbac)
    s6 = (- Caa) + ((1 - Yaa) * ((fva_aa * Cva) + (fbu_aa * Cbu) + (fpro_aa * Cpro) + (fac_aa * Cac))) + (Yaa * Cbac)
    s7 = (- Cfa) + ((1 - Yfa) * 0.7 * Cac) + (Yfa * Cbac)
    s8 = (- Cva) + ((1 - Yc4) * 0.54 * Cpro) + ((1 - Yc4) * 0.31 * Cac) + (Yc4 * Cbac)
    s9 = (- Cbu) + ((1 - Yc4) * 0.8 * Cac) + (Yc4 * Cbac)
    s10 = (- Cpro) + ((1 - Ypro) * 0.57 * Cac) + (Ypro * Cbac)
    s11 = (- Cac) + ((1 - Yac) * Cch4) + (Yac * Cbac)
    s12 = ((1 - Yh2) * Cch4) + (Yh2 * Cbac)
    s13 = (-Cbac) + Cxc
    
    s13_x_rho = s13 * (rho13 + rho14 + rho15 + rho16 + rho17 + rho18 + rho19)

    s_tup = (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12)
    
    rho_tup = (rho1, rho2, rho3, rho4, rho5, rho6, rho7, rho8, rho9, rho10, rho11, rho12)
    
    sum_skpk = 0
    
    for s, rho in zip(s_tup, rho_tup):
        sum_skpk += s * rho + s13_x_rho
    
    dt_S_IC = QV_ratio * (S_IC_in - S_IC) - sum_skpk - rho_T_10 #10

    #Rho sum for aftermost equations 
    rho_summ_13_19 = (rho13 + rho14 + rho15 + rho16 + rho17 + rho18 + rho19)

    
    dt_S_IN = QV_ratio * (S_IN_in - S_IN) - (Ysu * Nbac * rho5) + ((Naa - Yaa * Nbac) * rho6) - (Yfa * Nbac * rho7) - (Yc4 * Nbac * rho8) - (Yc4 * Nbac * rho9) - (Ypro * Nbac * rho10) - (Yac * Nbac * rho11) - (Yh2 * Nbac * rho12) + (Nbac - Nxc) * rho_summ_13_19 + ((Nxc - fxI_xc * Ni - fsI_xc * Ni - fpr_xc * Naa) * rho1) #11
    # used the Naa over the n_aa 
    
    dt_S_I = QV_ratio * (S_I_in - S_I) + fsI_xc * rho1 #12

    # Particulate Matter
        
    dt_X_c = QV_ratio * (X_xc_in - X_xc) - rho1 + rho_summ_13_19  #13 Is X_xc = X_c?
    dt_X_ch = QV_ratio * (X_ch_in - X_ch) + (fch_xc * rho1) - rho2 #14
    dt_X_pr = QV_ratio * (X_pr_in - X_pr) + (fpr_xc * rho1) - rho3 #15
    dt_X_li = QV_ratio * (X_li_in - X_li ) + (fli_xc * rho1) - rho4 #16 
    dt_X_su = QV_ratio * (X_su_in - X_su) + (Ysu * rho5) - rho13 #17
    dt_X_aa = QV_ratio * (X_aa_in - X_aa) + (Yaa * rho6) - rho14 #18
    dt_X_fa = QV_ratio * (X_fa_in - X_fa) + (Yfa * rho7) - rho15 #19
    dt_X_c4 = QV_ratio * (X_c4_in - X_c4) + (Yc4 * rho8) + (Yc4 * rho9) - rho16 #20
    dt_X_pro = QV_ratio * (X_pro_in - X_pro) + (Ypro * rho10)  - rho17 # 21
    dt_X_ac = QV_ratio * (X_ac_in - X_ac) + (Yac * rho11) - rho18 # 22
    dt_X_h2 = QV_ratio * (X_h2_in - X_h2) + (Yh2 * rho12) - rho19 # 23
    dt_X_I = QV_ratio * (X_I_in - X_I) + (fxI_xc * rho1) # 24

    # Cations and Anions
    
    dt_S_cat = QV_ratio * (S_cat_in - S_cat) #25
    dt_S_an = QV_ratio * (S_an_in - S_an) #26
    
    # Ions states

    dt_S_hva = -rho_a4 #27
    dt_S_hbu = -rho_a5 #28
    dt_S_hpro = -rho_a6 #29
    dt_S_hac = -rho_a7 #30
    dt_S_hco3 = -rho_a10 #31
    dt_S_nh3 = -rho_a11 #32
    
    # H+ algebraic equation
    
    ''' Moved this to the start

    S_nh4 = S_IN - S_nh3
    theta = S_cat + S_nh4 - S_hco3 - (S_hac / 64) - (S_hpro / 112) - (S_hbu / 160) - (S_hva / 208) - S_an
    
    S_H_ion_new = -(theta / 2) + .5 * np.power(np.power(theta, 2) + 4 * Kw, .5)

    '''
    # Gas equations
    V_ratio = (V_liq / V_gas)
    
    dt_S_gas_h2 = -((S_gas_h2 * qgas) / V_gas) + rho_T_8 * (V_ratio) #33
    dt_S_gas_ch4 = -((S_gas_ch4 * qgas) / V_gas) + rho_T_9 * (V_ratio) #34
    dt_S_gas_co2 = -((S_gas_co2 * qgas) / V_gas) + rho_T_10 * (V_ratio) #35

    dt_S_H_ion = 0

    return dt_S_su, dt_S_aa, dt_S_fa, dt_S_va, dt_S_bu, dt_S_pro, dt_S_ac, dt_S_h2, dt_S_ch4, dt_S_IC, dt_S_IN, dt_S_I, dt_X_c, dt_X_ch, dt_X_pr, dt_X_li, dt_X_su, dt_X_aa, dt_X_fa, dt_X_c4, dt_X_pro, dt_X_ac, dt_X_h2, dt_X_I, dt_S_cat, dt_S_an, dt_S_hva, dt_S_hbu, dt_S_hpro, dt_S_hac, dt_S_hco3, dt_S_nh3, dt_S_gas_h2, dt_S_gas_ch4, dt_S_gas_co2, dt_S_H_ion




#%%
# Turning results from array to dict








