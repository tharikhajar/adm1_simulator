
# Covnert simulation results from array to dict
import numpy as np
def array_to_dict(results):
    '''list -> (dict)

    Transform the list of results in a dictionary with the names of the results.
    
    '''
    keys = [
        'Monossacarídeos',
        'Aminoacids',
        'Fatty Acids',
        'Valeric Acid',
        'Butyric Acid',
        'Propionic Acid',
        'Acetic Acid',
        'Hydrogen (Liquid)',
        'Methane (Liquid)',
        'Soluble Inerts',
        'Composite Material',
        'Carbohydrates',
        'Proteins',
        'Lipids',
        'Monosaccharide Consumers',
        'Aminoacids Consumers',
        'Fatty Acids Consumers',
        'But/Val Acids Consumers',
        'Propionic Acid Consumers',
        'Acetic Acid Consumers',
        'Hydrogen Consumers',
        'Composite Inerts',
        'Valeric Conjugate',
        'Butyric Conjugate',
        'Propionic Conjugate',
        'Acetic Conjugate',
        'Inorganic Carbon',
        'Inorganic Nitrogen',
        'Cations',
        'Anions',
        'Carbonic Acid',
        'Ammonia',
        'Protons',
        'Hydrogen (Gas)',
        'Methane (Gas)',
        'Carbon Dioxide (Gas)'
    ]

    zip_for_dict = zip(keys, results)
    results_dict = dict(zip_for_dict)

    return results_dict

def pH_post_calculation(df):
    '''
    Input: dataframe with simulation results
    Output: dataframe with proton concentration column recalculated
    '''

    from ode import phys_par

    Kw = phys_par[3]
    
    df['NH4+'] = df['Inorganic Nitrogen'] - df['Ammonia']
    df['Carbon Dioxide (Liquid)'] = df['Inorganic Carbon'] - df['Carbonic Acid']

    df['Theta'] = (
        df['Cations'] + df['NH4+'] - df['Carbonic Acid']
        - (df['Acetic Conjugate'] / 64)
        - (df['Propionic Conjugate'] / 112)
        - (df['Butyric Conjugate'] / 160)
        - (df['Valeric Conjugate'] / 208)
        - df['Anions']
        )

    df['Protons'] = (
        (-1 * df['Theta'] / 2)
        + 0.5 * np.power(
            np.power(df['Theta'], 2) + 4 * Kw, .5
        )
    )

    df['pH'] = -1 * np.log10(df['Protons'])

    df.drop(['Theta'], axis=1, inplace=True)

    return df

def gas_pressure_post_calculation(df):
    '''
    Input: dataframe with simulation results
    Output: dataframe with partial pressure columns and gasflow rate
    '''

    from ode import phys_par

    R = phys_par[0]
    Top = phys_par[2]
    Patm = phys_par[16]
    pgas_h2o = phys_par[17]
    kp = phys_par[18]

    df['Pressure (H2)'] = df['Hydrogen (Gas)'] * ((R * Top) / 16)
    df['Pressure (CH4)'] = df['Methane (Gas)'] * ((R * Top) / 64)
    df['Pressure (CO2)'] = df['Carbon Dioxide (Gas)'] * R * Top
    df['Pressure (H20)'] = pgas_h2o
    df['Pressure'] = df['Pressure (H2)'] + df['Pressure (CH4)'] + df['Pressure (CO2)'] + pgas_h2o
    df['Gas Flow'] = kp * (df['Pressure'] - Patm) * (df['Pressure'] / Patm)

    return df