import dash
from dash_bootstrap_components._components.Col import Col
from dash_bootstrap_components._components.Row import Row
import dash_core_components as dcc
from dash_core_components.Loading import Loading
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from assets.style import color_p, input_style
import plotly.graph_objects as go
import pathlib

from app import app

layout = dbc.Container([
    #Main Row
    dbc.Row([
        dbc.Col([
            html.Br(),
            html.H6('''Correlação entre as variáveis do modelo'''),
            html.Br(),
            html.Br(),

            html.H6 ('''Selecione a variável que será comparada pela lista ao lado e observe a correlação
             de acordo com o mapa de calor logo abaixo.''' , style = {'fontSize': 14,'textAlign': 'justify'}), 
            html.H6('''Ao selecionar uma variável do mapa de calor, um gráfico mostrando a correlação entre as 
            duas variáveis e um gráfico de dispersão serão plotados.''' , style = {'fontSize': 14, 'textAlign': 'justify'}),
            html.H6('''Clique e arraste uma área no gráfico para dar zoom e analisar pontos específicos, dê um clique duplo no gráfico para retornar ao zoom original''' , style = {'fontSize': 14, 'textAlign': 'justify'}),

            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),

            dbc.Button(
                'Atualizar', 
                id='botao_teste',
                n_clicks = 0,
                style={'display': 'none', 'background-color': color_p['4green'],'width' : '180px'},
            ),
            html.Br(),
            html.Br(),
            dcc.Link(dbc.Button(
                'Visão geral', 
                id='botao_correlation',
                n_clicks = 0,
                style={'background-color': color_p['4purple'],'width' : '180px'}),
                href='/results'
            ),
            html.Br(),
            html.Br(),
            dcc.Link(dbc.Button(
                'Visão detalhada', 
                id='botao_overview',
                 n_clicks = 0,
                style={'background-color': color_p['4purple'], 'width' : '180px'}),
                href='/results/dashboard'
                        ),            

            html.Br(),
            html.Br(),

            dcc.Link(dbc.Button(
                'Retornar a tela inicial', 
                id='botao_input',
                n_clicks = 0,
                style={'background-color': color_p['4green'],'width' : '180px'}),
                href='/'
            ),
        ], className="col-xs-1 text-center", width = 2, style={'height': '100vh', 'background-color': color_p['grey3']}),        
        dbc.Col([
            dcc.Dropdown(
                id='correlation_target',
                options=[],
                value='S_gas_ch4',
                searchable=True,
                style=dict(width='100%'),
            ),
            dcc.Graph(
                id='correlation_heatmap'
            )
        ],className="col-xs-1 text-center", style={'height': '100vh',}, width=4),
        dbc.Col([
            html.Br(),
            dcc.Graph(id='correlation_time_series'),
            dcc.Graph(id='correlation_scatter')
        ], width=6),
        

        dbc.Button(
            'Dummy',
            id='dummy_corr',
            n_clicks=0,
            style = {'display': 'none'}
        )
    ]),
#End Main Row    
], fluid=True)