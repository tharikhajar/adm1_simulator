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
inert = 'Inertes'
micro = 'Microrganismos'

class Variable():
    def __init__(self, name, unit, vanilla, ionic,
    color='#264653', category=None, subcategory=None, values=None):

        self.name = name
        self.unit = unit
        self.color = color
        self.vanilla = vanilla
        self.ionic = ionic
        self.category = category
        self.subcategory = subcategory
        self.values = values

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
        category = sol_org,
        subcategory = diss_gas
    ),
    S_ch4 = Variable(
        name = 'Metano Dissolvido',
        unit = kg_COD,
        color = '#606c38',
        vanilla = True,
        ionic = False,
        category = sol_org,
        subcategory = diss_gas
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
        name = 'Carboidratos',
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
        category = part_org,
        subcategory = micro
    ),
    X_aa = Variable(
        name = 'Consumidores de Aminoácidos',
        unit = kg_COD,
        color = '#084c61',
        vanilla = True,
        ionic = False,
        category = part_org,
        subcategory = micro
    ),
    X_fa = Variable(
        name = 'Consumidores de Ácidos Graxos',
        unit = kg_COD,
        color = '#db3a34',
        vanilla = True,
        ionic = False,
        category = part_org,
        subcategory = micro
    ),  
    X_c4 = Variable(
        name = 'Consumidores de Ácidos Valérico e Butírico',
        unit = kg_COD,
        color = '#ffc857',
        vanilla = True,
        ionic = False,
        category = part_org,
        subcategory = micro
    ),  
    X_pro = Variable(
        name = 'Consumidores de Ácido Propiônico',
        unit = kg_COD,
        color = '#323031',
        vanilla = True,
        ionic = False,
        category = part_org,
        subcategory = micro
    ),
    X_ac = Variable(
        name = 'Consumidores de Ácido Acético',
        unit = kg_COD,
        color = '#9a031e',
        vanilla = True,
        ionic = False,
        category = part_org,
        subcategory = micro
    ),
    X_h2 = Variable(
        name = 'Consumidores de Hidrogênio Molecular',
        unit = kg_COD,
        color = '#5f0f40',
        vanilla = True,
        ionic = False,
        category = part_org,
        subcategory = micro
    ),
    X_I = Variable(
        name = 'Material Compósito Inerte',
        unit = kg_COD,
        color = '#495057',
        vanilla = True,
        ionic = False,
        category = part_org,
        subcategory = inert
    ),
    S_hva = Variable(
        name = 'Valérico Ionizado',
        unit = kg_COD,
        color = '#006400',
        vanilla = True,
        ionic = True,
        category = sol_org,
        subcategory = acid_org
    ),
    S_hbu = Variable(
        name = 'Butírico Ionizado',
        unit = kg_COD,
        color = '#38b000',
        vanilla = True,
        ionic = True,
        category = sol_org,
        subcategory = acid_org
    ),
    S_hpro = Variable(
        name = 'Propiônico Ionizado',
        unit = kg_COD,
        color = '#70e000',
        vanilla = True,
        ionic = True,
        category = sol_org,
        subcategory = acid_org
    ),
    S_hac = Variable(
        name = 'Acético Ionizado',
        unit = kg_COD,
        color = '#ccff33',
        vanilla = True,
        ionic = True,
        category = sol_org,
        subcategory = acid_org
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
        name = 'Cátions',
        unit = kmol,
        color = '#006466',
        vanilla = True,
        ionic = True,
        category = sol_inor,
        subcategory = None
    ),
    S_an = Variable(
        name = 'Ânions',
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
        category = sol_inor,
        subcategory = None
    ),
    S_nh3 = Variable(
        name = 'Amônia',
        unit = kmol,
        color = '#4ecdc4',
        vanilla = True,
        ionic = True,
        category = sol_inor,
        subcategory = None
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
        name = '2a9d8f',
        unit = bar,
        color = '#aacc00',
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
