# Influent characterization of cane-molasses vinasse from BARRERA et al. (2015)
substrate_composition = {
    'Soluble': { # kg COD m-3
        'Sugar': 33.73,
        'Amino Acid': 5.82,
        'Fatty Acid': 0.09,
        'Acetic Acid': 1.36,
        'Inert': 16.97,
        'Total': 57.97
    },
    'Particulate': { # kg COD m-3
        'Charbohydrate': 6.91,
        'Protein': 0.09,
        'Lipid': 0.14,
        'Inert': 0,
        'Composite': 0,
        'Total': 7.15 
    },
    'Total': 65.12, # kg COD m-3
    'Cation': 0.315, # kmol m-3
    'Anion': 0.073 # kmol m-3
}

# Microrganisms yield from substrate from BARRERA et al. (2015)
degraders_yield = { # kg COD_Xx / kg COD_Sx 
    'Sugar': 0.100,
    'Amino Acid': 0.080,
    'LCFA': 0.060,
    'Valerate and Butyrate': 0.060,
    'Propionate': 0.040,
    'Acetate': 0.050,
    'Hydrogen': 0.070,
    # SRB = Sulfate Reducing Bacteria
    'pSRB': 0.035, # p = propianate
    'aSRB': 0.041, # a = acetate
    'hSRB': 0.051  # h = hydrogenotrophic
}

# Monod maximum specific uptake rate from BARRERA et al. (2015)

monod_uptake = {
    'Sugar-Xsu': 30,
    'LCFA-Xfa': 6,
    'HVa_HBu-Xc4': 20,
    'HPr-Xpro': 16,
    'HAc-Xac': 12,
    'H2-Xh2': 43,
    'HPr-pSRB': 23,
    'HAc-aSRB': 18.5,
    'H2-hSRB': 63,
}

# Monod maximum specific uptake rate from BARRERA et al. (2015)