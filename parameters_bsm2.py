# This file holds the parameter set from Rosen; Jeppsson 2006 implementation of ADM1 within the BSM2 framework
# This implementation is intended for urban waste water digestion and is widely used as an implementation validadion

# Composite particulate fractional composition. sum of components must equal 1

particulate_composition = {
    'general': {
        'sol_inert': 0.1,
        'part_inert': 0.2,
        'carb': 0.2,
        'prot': 0.2,
        'lip': 0.3
    },
    # unit below: kmole N (kg COD)-1
    'nitrogen': {
        'Nxc': 0.0376/14,
        'Ni': 0.06/14,
        'Naa': 0.007
    },
    # unit below: kmole C (kg COD)-1
    'carbon': {
        'Cxc': 0.02786,
        'sol_inert': 0.03,
        'carb': 0.0313,
        'prot': 0.03,
        'lip': 0.022,
        'part_inert': 0.03
    }
}

