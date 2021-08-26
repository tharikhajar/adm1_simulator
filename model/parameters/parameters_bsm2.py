# This file holds the parameter set from Rosen; Jeppsson 2006 implementation of ADM1 within the BSM2 framework
# This implementation is intended for urban waste water digestion and is widely used as an implementation validadion
import numpy as np
# BSM2 Benchmark Results

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

    0.1526778706263, # S_IC 22
    0.1302298158037, # S_IN 23
    0.0400000000000, # S_cat 24
    0.0200000000000, # S_an 25

    np.power(10., -7.4655377698929), # H+ 26

    0.0115962470726, # S_hva 27
    0.0132208262485, # S_hbu 28
    0.0157427831916, # S_hpro 29
    0.1972411554365, # S_hac 30
    0.1427774793921, # S_hco3 31
    0.0040909284584, # S_nh3 32
    0.0000102410356, # S_gas_h2 33
    1.6256072099814, # S_gas_ch4 34
    0.0141505346784 # S_gas_co2 35

]