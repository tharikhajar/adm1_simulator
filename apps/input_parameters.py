#Importing Libraries
from dash.dependencies import Input, Output, State
from dash_bootstrap_components._components.Col import Col
from dash_core_components.Slider import Slider
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.Br import Br
from dash_html_components.Div import Div
from dash_html_components.H6 import H6
from numpy.core.fromnumeric import size

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
V_digestor = 80 # m³


# Layout

layout = dbc.Container([
    #Main Row
    dbc.Row([

        # Text Col
        dbc.Col([
        #region
            html.H2('''
            Simulador de Biodigestão Anaeróbica
            ''', style={"textAlign": "center"}),

            html.Br(),

            html.H6('''
            Este programa simula a biodigestão anaeróbia pelo modelo ADM1, retornando diversas viaráveis cálculadas pelo modelo, 
            como a produção de biogás, além de retornar uma estimativa econômica.''', style={"textAlign": "justify"}),
                
            html.Br(),

            html.H6('''
            Os campos requiridos ao lado prezam a simplicidade do uso do simulador, onde valores mais específicos (por exemplo, DQO de componentes
            específicos) se baseiam na literatura, mantendo a fidelidade ao processo dinâmico da biodigestão anaeróbia de efluentes domésticos.
            Sinta-se livre para alterar os valores de acordo com a sua necessidade.''', 
            style={"textAlign": "justify"}),

            html.Br(),

            html.H6('''
            As equações, parâmetros e variáveis se baseiam no modelo ADM1, desenvolvido pelo grupo IWA, e foram retiradas do artigo técnico de 
            ROSEN, C. e JEPPSSON, U "Aspects on ADM1 Implementation within the BSM2 Framework. Technical report" de Maio de 2006, que abordou a
            implementação do modelo matemático ADM1 para efluentes domésticos. 
            ''', 
            style={"textAlign": "justify"}),

            html.Br(),

            html.H6(
            html.Label(['Download do Artigo: ', html.A('Lund University', href='https://www.lunduniversity.lu.se/lup/publication/ae051f12-f038-47d4-9873-1eacad310c27',
            style = {"color": '#2F183C'})])
            , style={"textAlign": "center"}),

            html.Br(),
            html.Br(),
            html.Br(),

            html.Div([
                html.H6(''' Contato dos desenvolvedores''', 
                style = {'textAlign': 'left', 'color': 'white', 'fontSize': 16 }),
                html.H6('''Fernando Falat Rangel • fefalat@yahoo.com.br''', 
                style = {'textAlign': 'left', 'color': 'white', 'fontSize': 12 }),
                html.H6('Miguel Lopes Alcântara • miguel.l.alcantara@outlook.com', 
                style = {'textAlign': 'left', 'color': 'white', 'fontSize': 12 }),
                html.H6('Tharik de Oliveira Hajar • tharikhajar@gmail.com',
                style = {'textAlign': 'left', 'color': 'white', 'fontSize': 12 }),
            ])
        ],  width={'size': 4,},
            align='center',
            className='text-white',
            style={
                'height': '100vh',
                'background-color': color_p['4green']}),
        #endregion
        # Text Col End

        # Parameters Col
        dbc.Col([
            #region
            # Upper Row
            dbc.Row([
                # Mass input col
                dbc.Col([
                    html.H6(
                        'Massa de Substrato Produzido por Dia (kg massa úmida/dia)',
                        style={"textAlign": "center"}
                        ),
                    dcc.Input(            
                        id = 'massa_dia',
                        type = 'number',
                        value = 250,
                        debounce = True,
                        min = 0 , max = 10**7, step = 1,
                        required= True,
                        size = "50",
                        persistence = True, persistence_type = 'session',
                        style={'border-radius':input_style['border-radius'], 'text-align':'start'}          
                    ),
                ], 
                className="col-xs-1 text-center", 
                align="middle",
                width={"size": 4},
                style = {"padding": "10px"}
                ),
                
                # Volume input col
                dbc.Col([

                    dbc.Col([ #volumes info/input col
                    # HEADSPACE - READ ONLY

                        html.Br(),
                        html.Br(),

                        html.H6(
                            "Volume do Headspace (m³)",
                            id = 'headspacetooltip',
                        ),
                        dcc.Input(            
                            id = 'Volume_Headspace',
                            type = 'number',
                            value = 30,
                            debounce = True,
                            min = 0 , max = 10**6, step = 1,
                            required= True,
                            size = "100",
                            persistence = True, persistence_type = 'session', 
                            style={'border-radius':input_style['border-radius'], 'text-align':'start',},
                            readOnly = True
                        ),

                        dbc.Tooltip(
                            "Headspace é o volume dedicado para o gás dentro do biodigestor."
                            " Para alterar, acesse a aba de opções avançadas abaixo.",
                            target="headspacetooltip",
                         ),
                        dbc.Tooltip(
                            "Headspace é o volume dedicado para o gás dentro do biodigestor."
                            " Para alterar, acesse a aba de opções avançadas abaixo.",
                            target="Volume_Headspace",
                         ),                         

                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),


                        html.H6(
                            "Volume (m³)",
                        ),
                        # VOLUME SELECTION
                        dcc.Dropdown(
                            id = 'selecao_volume',
                            options = [{'label': 'Total', 'value': 'total'}, 
                                        {'label': 'Líquido', 'value': 'liq'}],
                            value = 'total',
                            searchable = True,
                            style = dict(width='100%')
                        ),

                        html.Br(),

                        # VOLUME VALUE INPUT 
                        dcc.Input(            
                            id = 'Volume_Input',
                            type = 'number',
                            value = V_digestor,
                            debounce = True,
                            min = 0 , max = 10**6, step = 1,
                            required= True,
                            size = "100",
                            persistence = True, persistence_type = 'session', 
                            style={'border-radius':input_style['border-radius'], 'text-align':'start',}
                        ),
                        # VOLUME LOGIC ARGUMENTS
                    ],
                    className="col-xs-1 text-center",           
                    align = 'center',
                    ), #end info col                

                ], width = {'size': 4}), #end volume col
                dbc.Col([
                    dbc.Col([ #graph scheme col
                        dcc.Loading(id='loading_volume',
                        type='circle',
                        children=[
                        dcc.Graph(
                        id='bar_volume_biodigestor',
                        config={'displayModeBar': False},
                        )]),
                    ],
                    align = 'center',
                    className="col-xs-1 text-center",
                    style = {"padding" : "45px"}
                    ),], 
                width = {'size': 4}),
            ], 
            justify="center", style = {'background-color': color_p['grey1'],"align-content":'center', 'height': '50vh'}, align ='center'),
#end upper row

            # ADVANCED OPTIONS TAB
            dbc.Row([
                dbc.Col([
                dbc.CardHeader(
                    dbc.Button(
                        "Opções Avançadas",
                        color = '#2F183C',
                        id = 'advanced_options_button',
                    ),
                ),
                dbc.Collapse([
                    dbc.Row([
                        #Advanced options: Headspace input
                        dbc.Col([
                            html.H6("Porcentagem do Headspace (%)"),
                            dcc.Input(            
                                id = 'parcela_gas',
                                type = 'number',
                                value = 30,
                                debounce = True,
                                min = 1 , max = 50, step = 1,
                                required= True,
                                size = "100",
                                persistence = True, persistence_type = 'session', 
                                style={'border-radius':input_style['border-radius'], 'text-align':'start',}
                                ),
                        ],
                        width = 12),
                        ], align = "start"),

                        html.Br(),

                        #Advanced options: Feed Slider
                        html.H6('Vazão de Alimentação (m³/dia)',
                            className='text-center'
                        ),
                        dbc.Col([
                            dcc.Slider( 
                            id = 'slider_diluição',
                            min = 1,
                            max = 1000,
                            step = 0.01,
                            value = 50,
                            persistence = True, persistence_type = 'session',
                            tooltip={
                            'always_visible': True,
                            'placement': 'bottom'},
                        ),
                    ],width=12),

                    html.H6("Fração de DQO (kg DQO/kg massa úmida do substrato)"),
                    #Advanced options: COD Slider
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
                    ),width=12, )
                ],
                id = "collapse_advanced_options",
                is_open = False,
                ),
                ], 
                className="col-xs-1 text-center", width = 12),
                dbc.Col(
                    html.H6(
                        id='slider_output_container',
                        children=[]
                    )
                ,
                width=12,
                className='text-center'),
                dbc.Col(
                    dcc.Link(dbc.Button(
                        'Simular',
                        id='botao_simular',
                        n_clicks = 0,
                        size='lg',
                        style={'background-color': color_p['4purple']}
                    ), href='/results')
                ,
                width=12,
                className='text-center'),

                #Dummy
                html.Div(id='oi')
            ],
            align = "start",
        style={'height': '50vh', 'background-color': color_p['grey3']}),#end row
    ], style={'height': '100vh', 'background-color': color_p['grey3']})
    #End Main Row
])
], fluid=True)