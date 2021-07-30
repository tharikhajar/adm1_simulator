
# Covnert simulation results from array to dict
import numpy as np
def array_to_dict(results):
    '''list -> (dict)

    Transform the list of results in a dictionary with the names of the results.
    
    '''
    keys = [
        'Monosaccharides',
        'Aminoacids',
        'Fatty Acids',
        'Valeric Acid',
        'Butiric Acid',
        'Propionic Acid',
        'Acetic Acid',
        'Hydrogen (Liquid)',
        'Methane (Liquid)',
        'Inorganic Carbon',
        'Inorganic Nitrogen',
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
        'Cations',
        'Anions',
        'Valeric Conjugate',
        'Butiric Conjugate',
        'Propionic Conjugate',
        'Acetic Conjugate',
        'Carbonic Acid',
        'Ammonia',
        'Hydrogen (Gas)',
        'Methane (Gas)',
        'Carbon Dioxide (Gas)',
        'Protons'
    ]

    # Transposing results
    

    if type(results) == 'numpy.ndarray':

        results = np.transpose(results)


    zip_for_dict = zip(keys, results)
    results_dict = dict(zip_for_dict)

    return results_dict