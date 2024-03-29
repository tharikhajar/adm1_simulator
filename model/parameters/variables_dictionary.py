# units
kg_COD = 'kg COD / m-3'
kmol = 'kmol / m-3'
bar = 'bar'

# categories

sol_org = 'Solúveis Orgânicos'
part_org = 'Material Particulado'
sol_inor = 'Inorgânicos Solúveis'
gas = 'Fase Gasosa'

# sub categories

diss_gas = 'Gases Dissolvidos'
acid_org = 'Ácidos Orgânicos'
de_prot = 'Ácidos Desprotonados'
prot = 'Ácidos Protonados'
inert = 'Inertes'
micro = 'Microrganismos'
ac_frac = 'Ionização Ácida'

class Variable():
    def __init__(self, name, unit, vanilla, ionic=False,
    color='#264653', category=None, subcategory=None, values=None,
    derivative=None):

        self.name = name
        self.unit = unit
        self.color = color
        self.vanilla = vanilla
        self.ionic = ionic
        self.category = category
        self.subcategory = subcategory
        self.values = values
        self.derivative = derivative

    def find_steady_state(self):
    # Takes in a list of results values for a state and finds when it 
    # reaches stationary
    
        for i in range(len(self.values) - 26):
            differences = []
            for j in range(25):
                average_value = (self.values[i] + self.values[i+j]) / 2
                differences.append(abs(self.values[i] - self.values[i+j]) / average_value)
            biggest_difference = max(differences)

            average_end = (self.values[i] + self.values[-1]) / 2
            difference_to_the_end = abs(self.values[i] - self.values[-1]) / average_end

            if biggest_difference <= 0.001 and difference_to_the_end <= 0.01:
                self.steady_index = i
                return i

        self.steady_index = None


variables_data = dict(
    S_su = Variable(
        name = 'Monossacarídeos',
        unit = kg_COD,
        color = '#f94144',
        vanilla = True,
        ionic = False,
        category = sol_org,
        subcategory = None
    ),
    S_aa = Variable(
        name = 'Aminoácidos',
        unit = kg_COD,
        color = '#90be6d',
        vanilla = True,
        ionic = False,
        category = sol_org,
        subcategory = None
    ),
    S_fa = Variable(
        name = 'Ácidos Graxos',
        unit = kg_COD,
        color = '#f8961e',
        vanilla = True,
        ionic = False,
        category = sol_org,
        subcategory = None
    ),
    S_va = Variable(
        name = 'Ácido Valérico',
        unit = kg_COD,
        color = '#1b4332',
        vanilla = True,
        ionic = False,
        category = sol_org,
        subcategory = acid_org
    ),
    S_bu = Variable(
        name = 'Ácido Butírico',
        unit = kg_COD,
        color = '#40916c',
        vanilla = True,
        ionic = False,
        category = sol_org,
        subcategory = acid_org
    ),
    S_pro = Variable(
        name = 'Ácido Propiônico',
        unit = kg_COD,
        color = '#74c69d',
        vanilla = True,
        ionic = False,
        category = sol_org,
        subcategory = acid_org
    ),
    S_ac = Variable(
        name = 'Ácido Acético',
        unit = kg_COD,
        color = '#b7e4c7',
        vanilla = True,
        ionic = False,
        category = sol_org,
        subcategory = acid_org
    ),
    S_h2 = Variable(
        name = 'Hidrogênio Molecular Dissolvido',
        unit = kg_COD,
        color = '#277da1',
        vanilla = True,
        ionic = False,
        category = None,
        subcategory = None
    ),
    S_ch4 = Variable(
        name = 'Metano Dissolvido',
        unit = kg_COD,
        color = '#606c38',
        vanilla = True,
        ionic = False,
        category = None,
        subcategory = None
    ),
    S_I = Variable(
        name = 'Inertes Solúveis',
        unit = kg_COD,
        color = '#d3d3d3',
        vanilla = True,
        ionic = False,
        category = sol_org,
        subcategory = inert
    ),
    X_xc = Variable(
        name = 'Material Compósito',
        unit = kg_COD,
        color = '#22223b',
        vanilla = True,
        ionic = False,
        category = part_org,
        subcategory = None
    ),
    X_ch = Variable(
        name = 'Polissacarídeos',
        unit = kg_COD,
        color = '#d62828',
        vanilla = True,
        ionic = False,
        category = part_org,
        subcategory = None
    ),
    X_pr = Variable(
        name = 'Proteínas',
        unit = kg_COD,
        color = '#43aa8b',
        vanilla = True,
        ionic = False,
        category = part_org,
        subcategory = None
    ),
    X_li = Variable(
        name = 'Lipídios',
        unit = kg_COD,
        color = '#f9c74f',
        vanilla = True,
        ionic = False,
        category = part_org,
        subcategory = None
    ),
    X_su = Variable(
        name = 'Consumidores de Monossacarídeos',
        unit = kg_COD,
        color = '#177e89',
        vanilla = True,
        ionic = False,
        category = None,
        subcategory = micro
    ),
    X_aa = Variable(
        name = 'Consumidores de Aminoácidos',
        unit = kg_COD,
        color = '#084c61',
        vanilla = True,
        ionic = False,
        category = None,
        subcategory = micro
    ),
    X_fa = Variable(
        name = 'Consumidores de Ácidos Graxos',
        unit = kg_COD,
        color = '#db3a34',
        vanilla = True,
        ionic = False,
        category = None,
        subcategory = micro
    ),  
    X_c4 = Variable(
        name = 'Consumidores de Ácidos Valérico e Butírico',
        unit = kg_COD,
        color = '#ffc857',
        vanilla = True,
        ionic = False,
        category = None,
        subcategory = micro
    ),  
    X_pro = Variable(
        name = 'Consumidores de Ácido Propiônico',
        unit = kg_COD,
        color = '#323031',
        vanilla = True,
        ionic = False,
        category = None,
        subcategory = micro
    ),
    X_ac = Variable(
        name = 'Consumidores de Ácido Acético',
        unit = kg_COD,
        color = '#9a031e',
        vanilla = True,
        ionic = False,
        category = None,
        subcategory = micro
    ),
    X_h2 = Variable(
        name = 'Consumidores de Hidrogênio Molecular',
        unit = kg_COD,
        color = '#5f0f40',
        vanilla = True,
        ionic = False,
        category = None,
        subcategory = micro
    ),
    X_I = Variable(
        name = 'Material Compósito Inerte',
        unit = kg_COD,
        color = '#495057',
        vanilla = True,
        ionic = False,
        category = None,
        subcategory = inert
    ),
    S_hva = Variable(
        name = 'Valerato',
        unit = kg_COD,
        color = '#006400',
        vanilla = True,
        ionic = True,
        category = ac_frac,
        subcategory = de_prot
    ),
    S_hbu = Variable(
        name = 'Butirato',
        unit = kg_COD,
        color = '#38b000',
        vanilla = True,
        ionic = True,
        category = ac_frac,
        subcategory = de_prot
    ),
    S_hpro = Variable(
        name = 'Propianato',
        unit = kg_COD,
        color = '#70e000',
        vanilla = True,
        ionic = True,
        category = ac_frac,
        subcategory = de_prot
    ),
    S_hac = Variable(
        name = 'Acetato',
        unit = kg_COD,
        color = '#ccff33',
        vanilla = True,
        ionic = True,
        category = ac_frac,
        subcategory = de_prot
    ),
    S_IC = Variable(
        name = 'Carbono Inorgânico',
        unit = kmol,
        color = '#1b263b',
        vanilla = True,
        ionic = False,
        category = sol_inor,
        subcategory = None
    ),
    S_IN = Variable(
        name = 'Nitrogênio Inorgânico',
        unit = kmol,
        color = '#778da9',
        vanilla = True,
        ionic = False,
        category = sol_inor,
        subcategory = None
    ),
    S_cat = Variable(
        name = 'Cátions Não Especificados',
        unit = kmol,
        color = '#006466',
        vanilla = True,
        ionic = True,
        category = sol_inor,
        subcategory = None
    ),
    S_an = Variable(
        name = 'Ânions Não Especificados',
        unit = kmol,
        color = '#4d194d',
        vanilla = True,
        ionic = True,
        category = sol_inor,
        subcategory = None
    ),
    S_hco3 = Variable(
        name = 'Ácido Carbônico',
        unit = kmol,
        color = '#ff6b6b',
        vanilla = True,
        ionic = True,
        category = ac_frac,
        subcategory = prot
    ),
    S_nh3 = Variable(
        name = 'Amônia',
        unit = kmol,
        color = '#4ecdc4',
        vanilla = True,
        ionic = True,
        category = ac_frac,
        subcategory = prot
    ),
    S_H_ion = Variable(
        name = 'Prótons',
        unit = kmol,
        color = '#aacc00',
        vanilla = True,
        ionic = True,
        category = sol_inor,
        subcategory = None
    ),
    S_gas_h2 = Variable(
        name = 'Hidrogênio Molecular',
        unit = bar,
        color = '#264653',
        vanilla = True,
        ionic = False,
        category = gas,
        subcategory = None
    ),
    S_gas_ch4 = Variable(
        name = 'Metano',
        unit = bar,
        color = '#2a9d8f',
        vanilla = True,
        ionic = False,
        category = gas,
        subcategory = None
    ),
    S_gas_co2 = Variable(
        name = 'Dióxido de Carbono',
        unit = bar,
        color = '#f4a261',
        vanilla = True,
        ionic = False,
        category = gas,
        subcategory = None
    )
) 
#%%

# %%
