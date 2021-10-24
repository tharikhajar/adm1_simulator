import dash
from dash_bootstrap_components._components.Col import Col
from dash_bootstrap_components._components.Row import Row
import dash_core_components as dcc
from dash_core_components.Loading import Loading
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash_html_components.Center import Center
from dash_html_components.H1 import H1
from dash_html_components.H6 import H6
from assets.style import color_p, input_style
import plotly.graph_objects as go
import pathlib

from app import app

layout = dbc.Container([
    #Main Row
    dbc.Row([
        #Financial Values Col
        #region
        dbc.Col([
            dbc.Row([
                #Generator Efficiency
                dbc.Col([

                    html.Br(),
                    html.Br(),
                    html.Br(),
    
                    html.H6(
                        "Eficiência do motogerador (%)",
                        style = {"textAlign": "center"}
                    ),
                    dcc.Input(
                        id='generator_efficiency_input',
                        type='number',
                        value=.32, min=0, max=1, step=0.01, debounce=True,
                        style={"width": 230, "height": 30, 'text-align': 'center', 'border-radius':input_style['border-radius']},
                    ),
                ], align = 'center'),
                #Energy Price Input
                dbc.Col([

                    html.Br(),
                    html.Br(),
                    html.Br(),
    
                    html.H6(
                        "Preço da energia (R$/kWh)",
                        style = {"textAlign": "center"}
                    ),
                    dcc.Input(
                        id='energy_price_input',
                        type="number",
                        value=0.41, min=0.01, max=5, step=0.01, debounce=True,
                        style={"width": 230, "height": 30, 'text-align': 'center','border-radius':input_style['border-radius']},
                    ),
                ], width = 12),
                
                html.Br(),
                html.Br(),
                html.Br(),

                dbc.Col(width = 12),

                html.Br(),
                html.Br(),
                html.Br(),

                #Financial overview text
                dbc.CardHeader(
                    html.Div(id = 'monthly_savings_div', 
                    style = {"color": "black", "textAlign": "center"}),
                ),
                #Buttons
                dbc.Col([

                    html.Br(),
                    html.Br(),
                    html.Br(),

                    dbc.Button(
                        'Atualizar', 
                        id='botao_teste_2',
                        n_clicks = 0,
                        style={'background-color': color_p['4green']},
                    ),

                    html.Br(),
                    html.Br(),
                    dcc.Link(dbc.Button(
                        'Correlação', 
                        id='botao_correlation',
                        n_clicks = 0,
                        style={'background-color': color_p['4purple']}),
                        href='/results/correlation'
                    ),
                    html.Br(),
                    html.Br(),

                    dcc.Link(dbc.Button(
                        'Retornar a tela inicial', 
                        id='botao_input',
                        n_clicks = 0,
                        style={'background-color': color_p['4purple']}),
                        href='/'
                    ),
                ], className="col-xs-1 text-center", align="start", width = 12)
            ])
        ], width = 2, style={'height': '100vh', 'background-color': color_p['grey3']}),
        #endregion

        #Simulation Results Col
        dbc.Col([
            #region
            dbc.Row([
                #Title
                dbc.Col([
                    html.H1(
                    "Resultados da simulação",
                    style={"textAlign": "center"}
                    ),
                ],
                className="col-xs-1 text-center", align="center", width = 12
                ),
                #Dropdowns
                dbc.Col([
                    dcc.Dropdown(
                    id='first_axis',
                    options=[],
                    value='S_gas_ch4',
                    searchable=True,
                    style=dict(width='90%'),
                    ),
                    dcc.Dropdown(
                    id='second_axis',
                    options=[],
                    value='q_gas',
                    searchable=True,
                    style=dict(width='90%'),
                    
                    ),
                ], style=dict(display='flex'),
                className="col-xs-1 text-center", align="start", width = 12),
                #Graph
                dbc.Col(
                    dcc.Graph( 
                    id='time_series'),
                className="col-xs-1 text-center", align="center", width = 12),
            ]),
            dbc.Row([
                dbc.Col([
                    dcc.Dropdown(
                    id='area_chart_group',
                    options=[],
                    value='Fase Gasosa',
                    searchable=True,
                    style=dict(width='90%'),
                    )
                ], style=dict(display='flex'),
                className="col-xs-1 text-center", align="start", width = 12),

                dbc.Col(
                    dcc.Graph(
                        id='area_chart'),
                className="col-xs-1 text-center", align="center", width = 12)
            ])
        ],
        width = 10, 
        style={'height': '100vh'},
        align='center',
        ),
        #endregion
    ]),
#End Main Row    
], fluid=True)