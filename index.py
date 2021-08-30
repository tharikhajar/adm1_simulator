import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash_html_components.Font import Font
import dash
from numpy.core.fromnumeric import var
from app import app
from app import server
import plotly.graph_objects as go
from plotly.subplots import make_subplots
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
    simulation.calculate_gas_flow_rate()

    simulation.set_simulation_status(status=1)
    return ''

@app.callback(Output('teste', 'figure'),
    [Input('first_axis', 'value'),
    Input('second_axis', 'value')])
def plot_test(variable_1, variable_2):

    while simulation.simulation_status == 0:
        time.sleep(.1)

    fig = make_subplots(specs=[[{'secondary_y': True}]])
    t = simulation.t
    for variable, axis in zip([variable_1, variable_2],[False, True]):
        variable_data = simulation.data[variable]
        y = variable_data.values
        variable_name = variable_data.name
        unit_of_measure = variable_data.unit
        color = variable_data.color
        steady_state_index = variable_data.find_steady_state()
        steady_time = t[steady_state_index]

        fig.add_trace(
            go.Scatter(
                x=t, y=y,
                name=variable_name, marker = dict(color=color),
                mode='lines'
                ),
            secondary_y=axis
        )
        fig.add_trace(
            go.Scatter(
                x=[steady_time, steady_time], y=[min(y), max(y)], 
                name= 'Estado Estacionário para: ' + variable_name, marker = dict(color=color),
                mode='lines'
                ),
            secondary_y=axis
        )
        fig.update_yaxes(title_text= f'{variable_name} ({unit_of_measure})', secondary_y=axis)
    fig.update_xaxes(title_text='Tempo (dias)')
    return fig

@app.callback([Output('first_axis', 'options'),
    Output('second_axis', 'options')],
    Input('botao_teste', 'n_clicks'))
def populate_dropdown(n_clicks):
    options = []
    while simulation.simulation_status == 0:
        time.sleep(.1)
    for variable in simulation.data.keys():
        options.append(
            {
                'label': simulation.data[variable].name,
                'value': variable
            }
        )
    return options, options

    
@app.callback(Output('dummy_botao_input', 'children'),
    Input('botao_input', 'n_clicks'))
def reset_simulation(n_clicks):
    simulation.set_simulation_status(status=0)
    return ''

if __name__ == '__main__':
    app.run_server(debug=True)