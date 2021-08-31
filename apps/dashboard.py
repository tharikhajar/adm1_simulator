import dash
import dash_core_components as dcc
from dash_core_components.Loading import Loading
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objects as go

import pathlib

from app import app


layout = html.Div([
    html.Div(
        html.H1(
            "Resultados da simulação", 
            style={"textAlign": "center"})),

    html.Div(
        dcc.Loading(children=[

        html.Div([
            dcc.Dropdown(
                id='first_axis',
                options=[],
                value='S_gas_ch4',
                searchable=True
            ),
            dcc.Dropdown(
                id='second_axis',
                options=[],
                value='q_gas',
                searchable=True
            )
        ]),
        html.Div(
            dcc.Graph(
            id='teste'
        ))
        ])
    ),

    # Financial Value
    html.Div([
        html.Div([
            dcc.Input(
                id='generator_efficiency_input',
                value=.32, min=0, max=1, step=0.01
            )
        ])
    ]),
        html.Div([
        html.Div([
            dcc.Input(
                id='energy_price_input',
                value=0.41, min=0.01, max=5, step=0.01
            )
        ]),
        html.Div(id = 'monthly_savings_div')
    ]),

    html.Div([
    dcc.Link(html.Button(
            'Retornar a tela inicial', 
            id='botao_input',
            n_clicks = 0,
        ), href='/'),
        html.Button(
            'hitme', 
            id='botao_teste',
            n_clicks = 0,
        )
        ])
])


