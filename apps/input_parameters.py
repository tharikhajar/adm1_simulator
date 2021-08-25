#Importing Libraries
from dash_core_components.Slider import Slider
from dash_html_components.H3 import H3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pathlib
# Importing support files
#from app import app
PATH = pathlib.Path(__file__).parent
# Connecting files (Include data paths below)

app = dash.Dash(__name__)

# Data manipulation (Import and clean data from support files)
DQO = 125 # kg/DQO parameters
pH = 7 
massa_dia = 3 #kg/m³
V_digestor_liq = 20 # m3
V_digestor_gas = 20 # m³

# Layout

app.layout = html.Div([
    html.H1('Insira os dados solicitados para a simulação: ', style={"textAlign": "center"}),

    html.Div([

        html.H3("Insira o Valor de DQO do composto que será digerido:"),

        dcc.Input(
            id = 'DQO',
            type = 'number',
            placeholder = 125,
            debounce = True,
            min = 0 , max = 10000, step = 0.01,
            minLength = 0, maxLength = 100,
            autoComplete = 'on',
            disabled = False,
            readOnly = False,
            required= True,
            size = "100"
        ),

    html.Br(),

        html.H3("Insira o Valor do pH do composto que será digerido:"),

        dcc.Input(
            id = 'pH',
            type = 'number',
            placeholder = 7,
            debounce = True,
            min = 0 , max = 14, step = 1,
            minLength = 0, maxLength = 100,
            autoComplete = 'on',
            disabled = False,
            readOnly = False,
            required= True,
            size = "100"
        ),
    
    html.Br(),

        html.H3("Insira a quantidade de massa (kg) inserida por dia"),

        dcc.Input(            
            id = 'massa_dia',
            type = 'number',
            placeholder = 10,
            debounce = True,
            min = 0 , max = 100000000, step = 10,
            minLength = 0, maxLength = 50,
            autoComplete = 'on',
            disabled = False,
            readOnly = False,
            required= True,
            size = "50"
        ),

    html.Br(),

        html.H3("Insira o volume líquido (m³) do biodigestor"),

        dcc.Input(            
            id = 'Volume_Liquido',
            type = 'number',
            placeholder = 80,
            debounce = True,
            min = 0 , max = 100000000, step = 10,
            minLength = 0, maxLength = 50,
            autoComplete = 'on',
            disabled = False,
            readOnly = False,
            required= True,
            size = "100"
        ),

    html.Br(),

        html.H3("Insira o volume do headspace (m³) do biodigestor"),

        dcc.Input(            
            id = 'Volume_Headspace',
            type = 'number',
            placeholder = 20,
            debounce = True,
            min = 0 , max = 100000000, step = 10,
            minLength = 0, maxLength = 50,
            autoComplete = 'on',
            disabled = False,
            readOnly = False,
            required= True,
            size = "100"
        ),                      
    ]),

html.Br(),

    html.Div([        
        dcc.Slider( 
            id = 'slider_diluição',
            min = 0,
            max = 20, # Dependes on unity  used L or m³?
            step = 1,
            value = 10
        ),
        html.Div(id='slider_output_container')
    ]),

html.Br(),
html.Br(),

        html.Button( #como conectar esse botão ao acionamento da resolução do modelo ADM-1?
            'SIMULAR', 
            id='botao_simular',
            n_clicks = 0,
        ),
])
# Callbacks

@app.callback(
    dash.dependencies.Output('slider_output_container', 'children'),
    [dash.dependencies.Input('slider_diluição', 'value')])
def update_output(value):
    return 'A diluição é de {} para massa.'.format(value)

# Run Server

if __name__ == '__main__':
    app.run_server(debug=True)


