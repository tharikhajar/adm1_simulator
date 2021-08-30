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
                value='S_gas_ch4'
            ),
            dcc.Dropdown(
                id='second_axis',
                options=[],
                value='q_gas'
            )
        ]),
        html.Div(
            dcc.Graph(
            id='teste'
        ))
        ])
    ),

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



# @app.callback(Output('teste', 'children'),
#     [Input('botao_input', 'n_clicks')])
# def test(n_clicks):
#     # simulation.calculate_parameters()
#     # simulation.simulate()
#     # value = simulation.results[0][0]
#     palavra = 'oi'
#     return n_clicks

# if __name__ == '__main__':
#     app.run_server(debug=False)