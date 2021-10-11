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
            dcc.Dropdown(
                id='correlation_target',
                options=[],
                value='S_gas_ch4',
                searchable=True,
                style=dict(width='40%'),
            ),
            dcc.Graph(
                id='correlation_heatmap'
            )
        ], width=4),
        

        dbc.Button(
            'Dummy',
            id='dummy_corr',
            n_clicks=0
        )
    ]),
#End Main Row    
], fluid=True)