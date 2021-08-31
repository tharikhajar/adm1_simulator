#Importing Libraries
from dash_core_components.Slider import Slider
from dash_html_components.H3 import H3


import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pathlib
from app import app

# app = dash.Dash(__name__)

# Data manipulation

DQO = 125 # kg/DQO parameters
pH = 7 
massa_dia = 3 #kg/m³
V_digestor_liq = 80 # m³
V_digestor_gas = V_digestor_liq * 0.3 # m³

# Layout

layout = html.Div([
    html.H1('Insira os dados solicitados para a simulação: ', style={"textAlign": "center"}),

    html.Div([

        html.H3("Fração de DQO do seu substrato (kg DQO/ kg Total)"),

        dcc.Input(
            id = 'DQO',
            type = 'number',
            value = 0.7,
            debounce = True,
            min = 0 , max = 1, step = 0.001,
            minLength = 0, maxLength = 100,
            autoComplete = 'on',
            disabled = False,
            readOnly = False,
            required= True,
            size = "100",
            persistence = True, persistence_type = 'session'
        
        ),

    html.Br(),

        html.H3("Massa total de substrato gerado (kg / dia)"),

        dcc.Input(            
            id = 'massa_dia',
            type = 'number',
            value = 10,
            debounce = True,
            min = 0 , max = 100000000, step = 1,
            minLength = 0, maxLength = 50,
            autoComplete = 'on',
            disabled = False,
            readOnly = False,
            required= True,
            size = "50",
            persistence = True, persistence_type = 'session'          
        ),
    
    html.Br(),

        html.H3("Valor do pH do substrato"),

        dcc.Input(
            id = 'pH',
            type = 'number',
            value = 7,
            debounce = True,
            min = 0 , max = 14, step = 0.1,
            minLength = 0, maxLength = 100,
            autoComplete = 'on',
            disabled = False,
            readOnly = False,
            required= True,
            size = "100",
            persistence = True, persistence_type = 'session'
        ),

    html.Br(),

        html.H3("Volume da parte líquida do biodigestor (m³)"),

        dcc.Input(            
            id = 'Volume_Liquido',
            type = 'number',
            value = V_digestor_liq,
            debounce = True,
            min = 0 , max = 100000000, step = 1,
            minLength = 0, maxLength = 50,
            autoComplete = 'on',
            disabled = False,
            readOnly = False,
            required= True,
            size = "100",
            persistence = True, persistence_type = 'session'
        ),

    html.Br(),

        html.H3("Insira o volume do headspace (m³) do biodigestor"),

        dcc.Input(            
            id = 'Volume_Headspace',
            type = 'number',
            value = V_digestor_gas,
            debounce = True,
            min = 0 , max = 100000000, step = 1,
            minLength = 0, maxLength = 50,
            autoComplete = 'on',
            disabled = False,
            readOnly = False,
            required= True,
            size = "100",
            persistence = True, persistence_type = 'session'
        ),                      
    ]),

    html.Br(),

    html.H3("Utilize o slider abaixo para selecionar a diluição desejada:"),

    html.Br(),

    html.Div(id='oi'),
    html.Div(id='dummy_botao_input'),

    html.Div([        
        dcc.Slider( 
            id = 'slider_diluição',
            min = 0.1,
            max = 200, # Dependes on unity  used L or m³?
            step = 0.1,
            value = 10,
            persistence = True, persistence_type = 'session',
            tooltip={
                    'always_visible': True,
                    'placement': 'bottom'
                }
        ),
    ]),

    html.Div(id='slider_output_container'),

    html.Br(),
    html.Br(),

        dcc.Link(html.Button( #como conectar esse botão ao acionamento da resolução do modelo ADM1?
            'SIMULAR', 
            id='botao_simular',
            n_clicks = 0,
        ), href='/results'),
])

# if __name__ == '__main__':
#     app.run_server(debug=False)
