import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_html_components.Div import Div

from app import app

from apps import dashboard, input_parameters

app.layout = html.Div ([
    html.Div([
        dcc.Link(html.Button('Inputs'), href='apps/input_parameters'),
        dcc.Link(html.Button('Outputs'), href='apps/dashboard')], 
        className = 'row'),

    dcc.location(id='url', refresh=False),
    html.Div(id='page-content', children=[])
])

@app.callback(Output('page-content', 'children'),[Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/apps/input_parameters':
        return input_parameters.layout
    if pathname == '/apps/dashboard':
        return dashboard.layout
    else:
        return "Erro 404 Página não encontrada, por favor selecione um link."

if __name__ == '__main__':
    app.run_server(debug=False)