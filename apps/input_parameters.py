#Importing Libraries
from dash_core_components.Slider import Slider
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.Br import Br

from app import app

from importlib import reload
import assets.style
reload(assets.style)
from assets.style import color_p, input_style



# app = dash.Dash(__name__)

# Data manipulation

DQO = 125 # kg/DQO parameters
pH = 7 
massa_dia = 3 #kg/m³
V_digestor_liq = 80 # m³
V_digestor_gas = V_digestor_liq * 0.3 # m³

# Layout

layout = dbc.Container([
    #Main Row
    dbc.Row([

        # Text Col
        dbc.Col([
        #region
            html.H2('''
            Simulalor de Biodigestão Anaeróbica
            ''', style={"textAlign": "center"}),
            html.H6('''
            Texto descritivo do programa, referência etc
            ''', style={"textAlign": "center"})
        ], width={'size': 6,},
            align='center',
            className='text-white',
            style={
                'height': '100vh',
                'background-color': color_p['4green']}),
        #endregion
        # Text Col End

        # Parameters Col
        dbc.Col([
            # Mass and pH
            #region
            dbc.Row([
                dbc.Col([
                    html.H6(
                        'Massa de Substrato Produzido por Dia (kg/dia)',
                        style={"textAlign": "center"}
                        ),
                    dcc.Input(            
                        id = 'massa_dia',
                        type = 'number',
                        value = 10,
                        debounce = True,
                        min = 0 , max = 10**7, step = 1,
                        required= True,
                        size = "50",
                        persistence = True, persistence_type = 'session',
                        style={'border-radius':input_style['border-radius']}          
                    ),
                ], className="col-xs-1 text-center"),
                dbc.Col([
                    html.H6(
                        'pH',
                        style={"textAlign": "center"}
                        ),
                    dcc.Input(
                        id = 'pH',
                        type = 'number',
                        value = 7,
                        debounce = True,
                        min = 0 , max = 14, step = 0.1,
                        required= True,
                        size = "100",
                        persistence = True, persistence_type = 'session',
                        style={'border-radius':input_style['border-radius']}
                    )
                ], className="col-xs-1 text-center")
                #endregion
            ]),

            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            # Volume
            #region
            dbc.Row([

                dbc.Col([

                        html.H6("Volume do Headspace (m³)"),

                        dcc.Input(            
                            id = 'Volume_Headspace',
                            type = 'number',
                            value = V_digestor_gas,
                            debounce = True,
                            min = 0 , max = 10**6, step = 1,
                            required= True,
                            size = "100",
                            persistence = True, persistence_type = 'session'
                        ),

                        html.H6("Volume Líquido (m³)"),

                        dcc.Input(            
                            id = 'Volume_Liquido',
                            type = 'number',
                            value = V_digestor_liq,
                            debounce = True,
                            min = 0 , max = 10**6, step = 1,
                            required= True,
                            size = "100",
                            persistence = True, persistence_type = 'session'
                        ),                  
                    ], className='col-xs-6 text-center'),

                dbc.Col([
                        dcc.Graph(
                            id='bar_volume_biodigestor',
                            config={'displayModeBar': False}
                            )
                     ], className='col-xs-6 text-center')
                    
                ]),
            #endregion
            #End Volume

            #DQO
            html.Br(),
            dbc.Row([
                dbc.Col(
                    html.H6('Fração de DQO (kg DQO/ kg Substrato (massa seca)',
                    className='text-center'
                    ),width=12),
                dbc.Col(
                dcc.Slider( 
                    id = 'slider_DQO',
                    min = 0.1,
                    max = 1,
                    step = 0.01,
                    value = 0.7,
                    persistence = True, persistence_type = 'session',
                    tooltip={
                            'always_visible': True,
                            'placement': 'bottom'
                        }
                ),width=12)
            ]),
            dbc.Row([
                dbc.Col(
                    html.H6('Vazão de Alimentação (m³/dia)',
                    className='text-center'
                    ),width=12),
                dbc.Col(
                dcc.Slider( 
                    id = 'slider_diluição',
                    min = 1,
                    max = 1000,
                    step = 1,
                    value = 50,
                    persistence = True, persistence_type = 'session',
                    tooltip={
                            'always_visible': True,
                            'placement': 'bottom'
                        }
                ),width=12),
                dbc.Col(
                    id='slider_output_container',
                    width=12
                ),
                dbc.Col(
                    dcc.Link(dbc.Button(
                        'Simular',
                        id='botao_simular',
                        n_clicks = 0,
                        size='lg',
                        style={'background-color': color_p['4purple']}
                    ), href='/results')
                , width=12,
                style={'height':100},
                className='text-center'),

                #Dummy
                html.Div(id='oi')
            ]),
            ], width=6,
            style={'height': '100vh'}),

    ], style={'height': '100vh'})
    #End Main Row
], fluid=True)