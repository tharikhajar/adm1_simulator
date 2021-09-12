# Dash Imports
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State



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

import assets.style
reload(assets.style)
from assets.style import color_p

simulation = Simulation('BSM2')


index_layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])
app.layout = index_layout

app.validation_layout = html.Div([
    index_layout,
    input_parameters.layout,
    dashboard.layout
])

# Pages url callback
#region
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
#endregion

# Homepage
#region

#Sldier de Vazão
#region
@app.callback([Output('slider_output_container', 'children'),
    Output('slider_diluição', 'max'),
    Output('slider_diluição', 'min'),
    Output('slider_diluição', 'marks'),
    Output('slider_diluição', 'step')],
    [Input('slider_diluição', 'value'),
    Input('massa_dia', 'value'),
    Input('Volume_Liquido', 'value')])
def update_output(dillution_rate, mass, V_liq):

    concentration = mass / dillution_rate
    HRT = round(V_liq / dillution_rate, 1)
    text_return = 'A concentração da alimentação é de {} kg substrato / m-3. Tempo de retenção hidráulica de {} dias'.format(round(concentration, 2), HRT)

    F_min = V_liq / 1000
    F_max = V_liq/10
    color = '#000000'
    marks = {
        F_min: {'label': "{}".format(F_min),
                'style': {'color': color}},
        F_max: {'label': "{}".format(F_max),
                'style': {'color': color}}
    }
    step_size = F_min

    return text_return, F_max, F_min, marks, step_size
#endregion

# Volume
@app.callback(Output('bar_volume_biodigestor', 'figure'),
            [Input('Volume_Liquido', 'value'),
            Input('Volume_Headspace', 'value')])
def plot_biodigestor_volume(V_liq, V_gas):

    data = [
        go.Bar(name='Volume de Líquido', x=[1], y=[V_liq],
            hovertemplate='%{label}', marker=dict(color=color_p['4purple'])),
        go.Bar(name='Volume de Gás', x=[1], y=[V_gas],
            hovertemplate='%{label}', marker=dict(color=color_p['4green'])),
        ]
    config=dict(displayModeBar=True)
    figbar = go.Figure(data=data)

    figbar.update_layout(
        xaxis = dict(
            showticklabels=False
        ),
        yaxis = dict(
            showticklabels=False
        ),
        showlegend=False,
        barmode='stack',
        width=120,
        height = 300, 
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0,
            pad=4
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
        )


    return figbar



#endregion

# Simulate
#region
@app.callback(Output('oi', 'children'),
    [Input('botao_simular', 'n_clicks')],
    [State('slider_DQO', 'value'),
    State('pH', 'value'),
    State('massa_dia', 'value'),
    State('Volume_Liquido', 'value'),
    State('Volume_Headspace', 'value'),
    State('slider_diluição', 'value')])
def simulate_test(n_clicks, DQO, pH, mass, V_liq, V_gas, dillution_rate):
    simulation.set_simulation_status(status=0)
    simulation.update_parameters(DQO, pH, dillution_rate, V_liq, V_gas, mass)
    simulation.calculate_parameters()
    simulation.simulate()
    simulation.calculate_gas_flow_rate()

    simulation.set_simulation_status(status=1)
    return ''
#endregion

# Dashboard
#region
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
                mode='lines', line = dict(dash='dash')
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

@app.callback(Output('monthly_savings_div', 'children'), 
    [Input('generator_efficiency_input', 'value'),
    Input('energy_price_input', 'value')])
def financial_calculation(generator_efficiency, energy_price):
    while simulation.simulation_status == 0:
        time.sleep(.1)
    simulation.calculate_financial_value(energy_price=energy_price, generator_efficiency=generator_efficiency)
    monthly_energy = round(simulation.monthly_energy,0)
    monthly_savings = round(simulation.monthly_savings, 2)
    return f'{monthly_energy} kWh gerados, resultando em uma economia de R$ {monthly_savings} ao mês'
#endregion


if __name__ == '__main__':
    app.run_server(debug=True)