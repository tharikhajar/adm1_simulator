import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash_html_components.Font import Font
import dash
from app import app
from app import server
import plotly.graph_objects as go
import time

from apps import input_parameters, dashboard
import pathlib
import model.ode_class

from importlib import reload
reload(input_parameters)
reload(dashboard)
reload(model.ode_class)

from model.ode_class import Simulation

simulation = Simulation('BSM2')

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    '''Displays page according to url adress, which is changed by the dcc.Link for each 'dashboard.py' and 'input_parametres.py'
    '''
    if pathname == '/results':
        return dashboard.layout
    elif pathname == '/':
        return input_parameters.layout
    else:
        return input_parameters.layout


@app.callback(Output('slider_output_container', 'children'),
    [Input('slider_diluição', 'value')])
def update_output(value):
    return 'A diluição é de {} para massa.'.format(value)


@app.callback(Output('oi', 'children'),
    [Input('botao_simular', 'n_clicks')],
    [State('DQO', 'value'),
    State('pH', 'value'),
    State('massa_dia', 'value'),
    State('Volume_Liquido', 'value'),
    State('Volume_Headspace', 'value'),
    State('slider_diluição', 'value')])
def simulate_test(n_clicks, DQO, pH, mass, V_liq, V_gas, dillution_rate):


    simulation.update_parameters(DQO, pH, dillution_rate, V_liq, V_gas, mass)
    simulation.calculate_parameters()
    simulation.simulate()
    return ''

@app.callback(Output('teste', 'figure'),
    [Input('botao_teste', 'n_clicks')])
def plot_test(n_clicks):

    time.sleep(10)
    y = simulation.results[0]
    t = simulation.t

    fig = go.Figure(data=go.Scatter(x=t, y=y))

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)