# This file holds the parameter set from Rosen; Jeppsson 2006 implementation of ADM1 within the BSM2 framework
# This implementation is intended for urban waste water digestion and is widely used as an implementation validadion
#%%
import numpy as np
# BSM2 Benchmark Results

S_su_in = 0.01 # kg COD m-3
S_aa_in = 0.001 # kg COD m-3
S_fa_in = 0.001 # kg COD m-3
S_va_in = 0.001 # kg COD m-3    
S_bu_in = 0.001 # kg COD m-3
S_pro_in = 0.001 # kg COD m-3
S_ac_in = 0.001 # kg COD m-3
S_h2_in = np.power(10., -8.) # kg COD m-3
S_ch4_in = np.power(10., -5.) # kg COD m-3
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

S_IC_in = 0.04 # kmole m-3
S_IN_in = 0.01 # kmole m-3
S_cat_in = 0.04 # kmole m-3
S_an_in = 0.02 # kmole m-3

feed_composition = [ #MHSG:indicar aqui ou no início do arquivo o que são estes números
    S_su_in, #0
    S_aa_in, #1
    S_fa_in, #2
    S_va_in, #3
    S_bu_in, #4
    S_pro_in, #5
    S_ac_in, #6
    S_h2_in, #7
    S_ch4_in, #8
    S_I_in, #9
    X_xc_in, #10
    X_ch_in, #11
    X_pr_in, #12
    X_li_in, #13
    X_su_in, #14
    X_aa_in, #15
    X_fa_in, #16
    X_c4_in, #17
    X_pro_in, #18
    X_ac_in, #19
    X_h2_in, #20
    X_I_in, #21
    S_IC_in, #22
    S_IN_in, #23
    S_cat_in, #24
    S_an_in #25
]

feed_composition_array = np.array(feed_composition)
DQO = sum(feed_composition_array[:-4])
feed_composition_ratios = feed_composition_array / DQO



#%%
# Initial Conditions / Variables

# Organics
S_su =  0.0124
S_aa =  0.0055
S_fa =  0.1074
S_va =  0.0123
S_bu = 0.0140
S_pro = 0.0176
S_ac =  0.0893
S_h2 =  2.5055*np.power(10., -7.)
S_ch4 = 0.0555
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
S_hva = 0.0123  
S_hbu = 0.0140
S_hpro =  0.0175 
S_hac =  0.0890   

# Inorganics
S_IC = 0.0951
S_IN = 0.0945
S_cat =  3.5659*np.power(10., -43.)
S_an =  0.0052
S_hco3 = 0.0857
S_nh3 = 0.0019

# H+ (pH)
S_H_ion = 5.4562*np.power(10., -8.)

# Gas states
S_gas_h2 = 1.1032*np.power(10.,-5.) 
S_gas_ch4 = 1.6535
S_gas_co2 = 0.0135

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
    S_I, #9
    X_xc, #10
    X_ch, #11
    X_pr, #12
    X_li, #13
    X_su, #14
    X_aa, #15
    X_fa, #16
    X_c4, #17
    X_pro, #18
    X_ac, #19
    X_h2, #20
    X_I, #21
    S_hva ,#22
    S_hbu, #23
    S_hpro, #24
    S_hac, #25

    S_IC, #26
    S_IN, #27
    S_cat, #28
    S_an, #29
    S_hco3, #30
    S_nh3 #31
] 

initial_condition_array = np.array(initial_conditions)
DQO_initial_condition = sum(initial_condition_array[:-6])
initial_condition_ratio = initial_condition_array / DQO_initial_condition
pH = -1 * np.log10(S_H_ion)

#%%

# This is not gonna be used. keeping here to have quick access to the order of the variables
# initial_conditions = [
#     S_su, #0
#     S_aa, #1
#     S_fa, #2
#     S_va, #3
#     S_bu, #4
#     S_pro, #5
#     S_ac, #6
#     S_h2, #7
#     S_ch4, #8
#     S_I, #9
#     X_xc, #10
#     X_ch, #11
#     X_pr, #12
#     X_li, #13
#     X_su, #14
#     X_aa, #15
#     X_fa, #16
#     X_c4, #17
#     X_pro, #18
#     X_ac, #19

#     X_h2, #20
#     X_I, #21

#     S_IC, #22
#     S_IN, #23
#     S_cat, #24
#     S_an, #25

#     S_H_ion, #26

#     S_hva ,#27
#     S_hbu, #28
#     S_hpro, #29
#     S_hac, #30
#     S_hco3, #31
#     S_nh3, #32
#     S_gas_h2, #33
#     S_gas_ch4, #34
#     S_gas_co2 #35
#     ] 


#Parameters

# Stoichiometric Parameters

fsI_xc = 0.1
fxI_xc = 0.2
fch_xc = 0.2
fpr_xc = 0.2
fli_xc = 0.3
Nxc = 0.0376 / 14. # kmole N (kg COD)-1
Ni = 0.06 / 14. # kmole N (kg COD)-1
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
Nbac = 0.08 / 14. # # kmole N (kg COD)-1
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
    Cch4, #38
    Yac, #39
    Yh2, #40
]


# Biochemical Parameters
Kdis = 0.5 # d-1
Khyd_ch = 10. # d-1
Khyd_pr = 10. # d-1
Khyd_li = 10. # d-1
Ks_in = np.power(10., -4.) # M
Km_su = 30. # d-1
Ks_su = 0.5 # kg COD m-3
pHul_aa = 5.5
pHll_aa = 4.
km_aa = 50. # d-1
Ks_aa = 0.3 # kg COD m-3
km_fa = 6. # d-1
Ks_fa = 0.4 # kg COD m-3
Kih2_fa = 5. * np.power(10.,-6.) # kg COD m-3
km_c4 = 20. # d-1
Ks_c4 = 0.2 # kg COD m-3
Kih2_c4 = np.power(10., -5.) # kg COD m-3
km_pro = 13. # d-1
Ks_pro = 0.1 # kg COD m-3
Kih2_pro = 3.5 * np.power(10., -6.) # kg COD m-3
km_ac = 8. # d-1
Ks_ac = 0.15 # kg COD m-3
Ki_nh3 = 0.0018 # M
pHul_ac = 7.
pHll_ac = 6.
km_h2 = 35. # d-1
Ks_h2 = 7. * np.power(10., -6.) # kg COD m-3
pHul_h2 = 6.
pHll_h2 = 5.
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
kLa = 200. # d-1
Kh_co2 = 0.035 * np.exp((-19410 / (R * 100)) * t_inv_dif)
Kh_ch4 = 0.0014 * np.exp((-14240/(R * 100)) * t_inv_dif)
Kh_h2 = (7.8 * np.power(10., -4.)) * np.exp((-4180 / (R * 100)) * t_inv_dif)
V_liq = 3400. # m^3
V_gas = 300. # m^3
Q_in = 170. # m^3 d-1


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
    Kh_h2 #22
]


BSM2_results = [
    0.0119548297170, # S_su 0
    0.0053147401716, # S_aa 1
    0.0986214009308, # S_fa 2
    0.0116250064639, # S_va 3
    0.0132507296663, # S_bu 4
    0.0157836662845, # S_pro 5
    0.1976297169375, # S_ac 6
    0.0000002359451, # S_h2 7
    0.0550887764460, # S_ch4 8
    0.3286976637215, # S_I 9
    0.3086976637215, # X_xc 10
    0.0279472404350, # X_Ch 11
    0.1025741061067, # X_pr 12
    0.0294830497073, # X_li 13
    0.4201659824546, # X_su 14
    1.1791717989237, # X_aa 15
    0.2430353447194, # X_fa 16
    0.4319211056360, # X_c4 17
    0.1373059089340, # X_pro 18
    0.7605626583132, # X_ac 19
    0.3170229533613, # X_h2 20
    25.6173953274430, # X_I 21
    0.0115962470726, # S_hva 22
    0.0132208262485, # S_hbu 23
    0.0157427831916, # S_hpro 24
    0.1972411554365, # S_hac 25

    0.1526778706263, # S_IC 26
    0.1302298158037, # S_IN 27
    0.0400000000000, # S_cat 28
    0.0200000000000, # S_an 29
    0.1427774793921, # S_hco3 30
    0.0040909284584, # S_nh3 31

    np.power(10., -7.4655377698929), # H+ 32

    0.0000102410356, # S_gas_h2 33
    1.6256072099814, # S_gas_ch4 34
    0.0141505346784 # S_gas_co2 35

]

BSM2_parameters = dict(
    feed_composition_ratios = feed_composition_ratios,
    initial_condition = dict(
        initial_condition_ratio = initial_condition_ratio,
        pH = pH,
        gas_initial_state = gas_initial_state
    ),
    stc_par = stc_par,
    bioch_par = bioch_par,
    phys_par = dict(
        phys_par = phys_par,
        V_liq = V_liq,
        V_gas = V_gas,
        Q_in = Q_in
    ),
    DQO=DQO,
    DQO_initial_condition = DQO_initial_condition,
    mass=1,
    dillution_rate=1
)