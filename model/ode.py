# File dedicated for the implementation of the ODE model
import numpy as np

def adm1_ode(t, initial_conditions, stc_par, bioch_par, phys_par, feed_composition):

    # Feed Composition


    S_su_in, S_aa_in, S_fa_in, S_va_in, S_bu_in = feed_composition[0:5]
    S_pro_in, S_ac_in, S_h2_in, S_ch4_in, S_I_in  = feed_composition[5:10]
    X_xc_in, X_ch_in, X_pr_in, X_li_in, X_su_in = feed_composition[10:15]
    X_aa_in, X_fa_in, X_c4_in, X_pro_in, X_ac_in = feed_composition[15:20]
    X_h2_in, X_I_in, S_IC_in, S_IN_in, S_cat_in = feed_composition[20:25]
    S_an_in = feed_composition[25]


    # Variables
    
    S_su, S_aa, S_fa, S_va, S_bu = initial_conditions[0:5]
    S_pro, S_ac, S_h2, S_ch4, S_I = initial_conditions[5:10]
    X_xc, X_ch, X_pr, X_li, X_su = initial_conditions[10:15]
    X_aa, X_fa, X_c4, X_pro, X_ac = initial_conditions[15:20]
    X_h2, X_I, S_hva, S_hbu, S_hpro  = initial_conditions[20:25]
    S_hac, S_IC, S_IN, S_cat, S_an,   = initial_conditions[25:30]
    S_hco3, S_nh3, S_H_ion, S_gas_h2, S_gas_ch4 = initial_conditions[30:35]
    S_gas_co2 = initial_conditions[35]

    # Stoichimetric Parameters
    
    fsI_xc, fxI_xc, fch_xc, fpr_xc, fli_xc = stc_par[0:5]
    Nxc, Ni, Naa, Cxc, CsI = stc_par[5:10]
    Cch, Cpr, Cli, CxI, Csu = stc_par[10:15]
    Caa, ffa_li, Cfa, fh2_su, fbu_su = stc_par[15:20]
    fpro_su, fac_su, Nbac, Cbu, Cpro = stc_par[20:25]
    Cac, Cbac, Ysu, fh2_aa, fva_aa = stc_par[25:30]
    fbu_aa, fpro_aa, fac_aa, Cva, Yaa = stc_par[30:35]
    Yfa, Yc4, Ypro, Cch, Yac = stc_par[35:40]
    Yh2 = stc_par[40] 


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


    # Hill inhibition function based on hydrogen ions (pH Inhibition)
    # Eq (3.2) p.7
    Kph_aa = np.power(10., -((pHll_aa + pHul_aa) / 2.)) 
    Kph_ac = np.power(10., -((pHll_ac + pHul_ac) / 2.))
    Kph_h2 = np.power(10., -((pHll_h2 + pHul_h2) / 2.))

    n_aa = 3. / (pHul_aa - pHll_aa) 
    n_ac = 3. / (pHul_ac - pHll_ac)
    n_h2 = 3. / (pHul_h2 - pHll_h2)

    KpH_n_aa = np.power(Kph_aa, n_aa)
    I_pH_aa = KpH_n_aa / (KpH_n_aa + np.power(S_H_ion, n_aa))
    KpH_n_ac = np.power(Kph_ac, n_ac)
    I_pH_ac = KpH_n_ac / (KpH_n_ac + np.power(S_H_ion, n_ac))
    KpH_n_h2 = np.power(Kph_h2, n_h2)
    I_pH_h2 = KpH_n_h2 / (KpH_n_h2 + np.power(S_H_ion, n_h2))

    I_IN_lim = 1. / (1. + (Ks_in / S_IN))
    I_h2_fa = 1. / (1. + (S_h2 / Kih2_fa))
    I_h2_c4 = 1. / (1. + (S_h2 / Kih2_c4))
    I_h2_pro = 1. / (1. + (S_h2 / Kih2_pro))
    I_nh3 = 1. / (1. + (S_nh3 / Ki_nh3))
    
    I5 = I6 = I_pH_aa * I_IN_lim
    I7 = I_pH_aa * I_IN_lim * I_h2_fa
    I8 = I9 = I_pH_aa * I_IN_lim * I_h2_c4
    I10 = I_pH_aa * I_IN_lim * I_h2_pro
    I11 = I_pH_ac * I_IN_lim * I_nh3
    I12 = I_pH_h2 * I_IN_lim
    

    # Biochemical process rates 

    rho1 = Kdis * X_xc # Particulate matter disintegration
    rho2 = Khyd_ch * X_ch # Carbohydrate Hydrolysis
    rho3 = Khyd_pr * X_pr # Prtotein Hydrolysis
    rho4 = Khyd_li * X_li # Lipids Hydrolysis
    rho5 = Km_su * (S_su / (Ks_su + S_su)) * X_su * I5 # Monosaccharides Comsumption
    rho6 = km_aa * (S_aa / (Ks_aa + S_aa)) * X_aa * I6 # Aminoacids Comsumption
    rho7 = km_fa * (S_fa / (Ks_fa + S_fa)) * X_fa * I7 # Fatty Acids Comsumption
    rho8 = km_c4 * (S_va / (Ks_c4 + S_va)) * X_c4 * (S_va / (S_bu + S_va + np.power(10.,-6.))) * I8 # Valeric Comsumption
    rho9 = km_c4 * (S_bu / (Ks_c4 + S_bu)) * X_c4 * (S_bu / (S_bu + S_va + np.power(10.,-6.))) * I9 # Butyric Comsumption
    rho10 = km_pro * (S_pro / (Ks_pro + S_pro)) * X_pro * I10 # Propionic Comsumption
    rho11 = km_ac * (S_ac / (Ks_ac + S_ac)) * X_ac * I11 # Acetic Comsumption
    rho12 = km_h2 * (S_h2 / (Ks_h2 + S_h2)) * X_h2 * I12 # Molecular Hydrogen Comsumption
    rho13 = kdec_Xsu * X_su # Decay of micoorganisms consumers of monosaccharides 
    rho14 = kdec_Xaa * X_aa # Decay of micoorganisms consumers of aminoacids
    rho15 = kdec_Xfa * X_fa # Decay of micoorganisms consumers of fat acids
    rho16 = kdec_Xc4 * X_c4 # Decay of micoorganisms consumers of valeric and butiric acids
    rho17 = kdec_Xpro * X_pro # Decay of micoorganisms consumers of propionic acid
    rho18 = kdec_Xac * X_ac # Decay of micoorganisms consumers of acetic acid
    rho19 = kdec_Xh2 * X_h2 # Decay of micoorganisms consumers of hydrogen


    # Acid-base rates 
    
    rho_a4 = kA_Bva * ( S_hva * (Ka_va + S_H_ion) - Ka_va * S_va) # for Valeric Acid
    rho_a5 = kA_Bbu * ( S_hbu * (Ka_bu + S_H_ion) - Ka_bu * S_bu) # for Butyric Acid
    rho_a6 = kA_Bpro * ( S_hpro * (Ka_pro + S_H_ion) - Ka_pro * S_pro) # for Propionic Acid
    rho_a7 = kA_Bac * ( S_hac * (Ka_ac + S_H_ion) - Ka_ac * S_ac) # for Acetic Acid
    rho_a10 = kA_Bco2 * ( S_hco3 * (Ka_co2 + S_H_ion) - Ka_co2 * S_IC) # for Carbonic Acid
    rho_a11 = kA_BIN * ( S_nh3 * (Ka_IN + S_H_ion) - Ka_IN * S_IN) # for Ammonia


    # Gas transfer rates
    
    pgas_h2 = S_gas_h2 * ((R * Top) / 16) # used in rho_T_8 
    pgas_ch4 = S_gas_ch4 * ((R * Top) / 64) # used in rho_T_9
    pgas_co2 = S_gas_co2 * R * Top # used in rho_T_10
    
    S_co2 = S_IC - S_hco3

    rho_T_8 = kLa * (S_h2 - 16 * Kh_h2 * pgas_h2) # Molecular Hydrogen 
    rho_T_9 = kLa * (S_ch4 - 64 * Kh_ch4 * pgas_ch4) # Methane 
    rho_T_10 = kLa * (S_co2 - Kh_co2 * pgas_co2) # Carbon Dioxide

    Pgas = pgas_h2 + pgas_ch4 + pgas_co2 + pgas_h2o # Headspace Pressure

    qgas = kp * (Pgas - Patm) #* (Pgas / Patm) # Gas flow rate #MHSG: tem certeza que é esta equação que usaram? lendo o texto, entendi que usaram aquela sem a fração no final. Eu indicaria o número da equação, mas, vejam só, o autor não numerou!

    
    # Differential Equations
    
    # Water Phase Equations
    # Soluble Matter

    QV_ratio = (Q_in/V_liq) #Dilution rate
    
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

    s_list = np.array([s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12]) 
    
    rho_list = np.array([rho1, rho2, rho3, rho4, rho5, rho6, rho7, rho8, rho9, rho10, rho11, rho12]) 
    
    sum_skpk = sum(s_list * rho_list) + s13_x_rho
    

    
    dt_S_IC = QV_ratio * (S_IC_in - S_IC) - sum_skpk - rho_T_10 #10

    #Rho sum for dt_X_c & dr_S_IN equations (biomass decay -> particulate matter & Inorganic Nitrogen) 
    rho_sum_13_19 = rho13 + rho14 + rho15 + rho16 + rho17 + rho18 + rho19
    
    dt_S_IN = QV_ratio * (S_IN_in - S_IN) - (Ysu * Nbac * rho5) + ((Naa - Yaa * Nbac) * rho6) - (Yfa * Nbac * rho7) - (Yc4 * Nbac * rho8) - (Yc4 * Nbac * rho9) - (Ypro * Nbac * rho10) - (Yac * Nbac * rho11) - (Yh2 * Nbac * rho12) + (Nbac - Nxc) * rho_sum_13_19 + ((Nxc - fxI_xc * Ni - fsI_xc * Ni - fpr_xc * Naa) * rho1) #11
    # used the Naa over the n_aa 
    
    dt_S_I = QV_ratio * (S_I_in - S_I) + fsI_xc * rho1 #12

    # Particulate Matter
        
    dt_X_xc = QV_ratio * (X_xc_in - X_xc) - rho1 + rho_sum_13_19  #13 Is X_xc = X_c?
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
    
    # Gas equations

    V_ratio = (V_liq / V_gas)
    
    dt_S_gas_h2 = -((S_gas_h2 * qgas) / V_gas) + rho_T_8 * (V_ratio) #33
    dt_S_gas_ch4 = -((S_gas_ch4 * qgas) / V_gas) + rho_T_9 * (V_ratio) #34
    dt_S_gas_co2 = -((S_gas_co2 * qgas) / V_gas) + rho_T_10 * (V_ratio) #35

    # H+ 

    S_nh4 = S_IN - S_nh3 
    theta = S_cat + S_nh4 - S_hco3 - (S_hac / 64) - (S_hpro / 112) - (S_hbu / 160) - (S_hva / 208) - S_an
    new_S_H_ion = (-1) * (theta / 2.) + (.5 * np.sqrt(np.power(theta, 2.) + 4. * Kw))

    dt_S_H_ion = new_S_H_ion - S_H_ion
    #        0       1       2        3        4        5         6         7       8           9       10      11      12       13       14        15      16       17       18        19        20        21    22        23         24        25        26       27       28        29       30         31          32        33            34          35                    
    return dt_S_su, dt_S_aa, dt_S_fa, dt_S_va, dt_S_bu, dt_S_pro, dt_S_ac, dt_S_h2, dt_S_ch4, dt_S_I, dt_X_xc, dt_X_ch, dt_X_pr, dt_X_li, dt_X_su, dt_X_aa, dt_X_fa, dt_X_c4, dt_X_pro, dt_X_ac, dt_X_h2, dt_X_I, dt_S_hva, dt_S_hbu, dt_S_hpro, dt_S_hac, dt_S_IC, dt_S_IN, dt_S_cat, dt_S_an, dt_S_hco3, dt_S_nh3, dt_S_H_ion, dt_S_gas_h2, dt_S_gas_ch4, dt_S_gas_co2 




