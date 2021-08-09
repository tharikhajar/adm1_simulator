import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_html_components.Font import Font

from app import app
from app import server

from apps import input_parameters, dashboard


app.layout = html.Div([
    html.H1("Simulação da produção de biogás", style={'color': 'green', 'fontsize':40, 'textAlign': 'center'}),
    html.H6("Software desenvolvido por Alcântara, Falat & Hajar baseado no modelo ADM1.", style = {'textAlign' : 'center', 'fontsize' : 15}),

html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link(html.Button('Inserir ou modificar Dados'), href='/apps/input_parameters'),
        dcc.Link(html.Button('Resultados'), href='/apps/dashboard'),
    ], className="row"),
    html.Div(id='page-content', children=[])
])])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/input_parameters':
        return input_parameters.layout
    if pathname == '/apps/dashboard':
        return dashboard.layout
    else:
        return "Ops! Parece que você está perdido... Erro 404: página não encontrada. Por favor selecione um botão."

if __name__ == '__main__':
    app.run_server(debug=False)