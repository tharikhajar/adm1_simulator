# Dash Imports
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash_html_components.Strong import Strong
from scipy import stats


from numpy.core.fromnumeric import var
from numpy.lib.arraysetops import unique
from app import app
from app import server
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

from apps import input_parameters, dashboard, correlation, overview
import pathlib
import model.ode_class

from importlib import reload
reload(input_parameters)
reload(dashboard)
reload(correlation)
reload(overview)
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
    dashboard.layout,
    correlation.layout
])

# Pages url callback
#region
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    '''Displays page according to url adress, which is changed by the dcc.Link for each 'dashboard.py' and 'input_parametres.py'
    '''
    if pathname == '/results':
        return overview.layout
    elif pathname == '/':
        return input_parameters.layout
    elif pathname == '/results/correlation':
        return correlation.layout
    elif pathname == '/results/dashboard' :
        return dashboard.layout
    else:
        return input_parameters.layout
#endregion

# Homepage
#region

#Slider da Vazão de alimentação e cálculo do tempo de retenção
#region
@app.callback([Output('slider_output_container', 'children'),
    Output('slider_diluição', 'max'),
    Output('slider_diluição', 'min'),
    Output('slider_diluição', 'marks'),
    Output('slider_diluição', 'step')],
    [Input('slider_diluição', 'value'),
    Input('massa_dia', 'value'),
    Input('Volume_Input', 'value'),
    Input('selecao_volume', 'value'),
    Input('parcela_gas', 'value')])
def update_output(dillution_rate, mass, V, V_type, parc_gas):

    parc_gas = parc_gas / 100
    if V_type == 'total':
        V_liq = V * (1 - parc_gas)
    else:
        V_liq = V

    concentration = mass / dillution_rate
    HRT = round(V_liq / dillution_rate, 1)
    text_return = 'A concentração da alimentação é de {} kg de substrato por m³. O tempo de retenção hidráulica é de {} dias'.format(round(concentration, 2), HRT)

    F_min = round(V_liq / 1000, 2)
    F_max = round(V_liq/10, 2)
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
@app.callback([Output('bar_volume_biodigestor', 'figure'),
            Output('Volume_Headspace', 'value')],
            [Input('Volume_Input', 'value'),
            Input('selecao_volume', 'value'),
            Input('parcela_gas', 'value')])
def plot_biodigestor_volume(V, V_type, parc_gas):

    parc_gas = parc_gas / 100
    if V_type == 'total':
        V_liq = round(V * (1 - parc_gas), 1)
        V_gas = round(V * parc_gas, 1)
    else:
        V_liq = round(V, 1)
        V_gas = round((V / (1 - parc_gas)) * parc_gas, 1)

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


    return figbar, V_gas



#endregion

# Simulate
#region
@app.callback(Output('oi', 'children'),
    [Input('botao_simular', 'n_clicks')],
    [State('slider_DQO', 'value'),
    State('massa_dia', 'value'),
    State('Volume_Input', 'value'),
    State('parcela_gas', 'value'),
    State('slider_diluição', 'value'),
    State('selecao_volume', 'value')])
def simulate_test(n_clicks, DQO, mass, V, parc_gas, dillution_rate, V_type):

    parc_gas = parc_gas / 100
    if V_type == 'total':
        V_liq = V * (1 - parc_gas)
        V_gas = V * parc_gas
    else:
        V_liq = V
        V_gas = (V / (1 - parc_gas)) * parc_gas


    simulation.set_simulation_status(status=0)
    simulation.update_parameters(DQO, dillution_rate, V_liq, V_gas, mass)
    simulation.calculate_parameters()
    simulation.simulate()
    simulation.calculate_gas_flow_rate()

    simulation.set_simulation_status(status=1)
    return ''
#endregion

# Overview
# Flow Rate chart
@app.callback(Output('time_series_gas', 'figure'),
    Input('botao_teste', 'n_clicks'))
def plot_time_series(n_clicks):

    while simulation.simulation_status == 0:
        time.sleep(.1)

    fig = make_subplots(specs=[[{'secondary_y': True}]])
    t = simulation.t
    t_init_index = 0
    t_init = 0
    while t_init < 1:
        t_init_index += 1
        t_init = t[t_init_index]

    variable_data = simulation.data['q_gas']
    y_max = 1.05 * max(variable_data.values[t_init_index:])
    
    for variable in ['q_gas', 'q_metane']:
        variable_data = simulation.data[variable]
        y = variable_data.values
        variable_name = variable_data.name
        unit_of_measure = variable_data.unit
        color = variable_data.color
        steady_state_index = variable_data.find_steady_state()
        steady_time = t[steady_state_index]

        fig.add_trace(
            go.Scatter(
                x=t[t_init_index:], y=y[t_init_index:],
                name=variable_name, marker = dict(color=color),
                mode='lines'
                )
        )
        fig.add_trace(
            go.Scatter(
                x=[steady_time, steady_time], y=[0, y_max], 
                name= 'Estado Estacionário para: ' + variable_name, marker = dict(color=color),
                mode='lines', line = dict(dash='dash')
                )
        )
        fig.update_yaxes(title_text= f'Vazão ({unit_of_measure})')
    fig.update_xaxes(title_text='Tempo (dias)')

    fig.update_layout(
        yaxis_range=[0, y_max],
        height=400,
        hovermode='x unified',
        margin=dict(
            l=15,
            r=15,
            b=15,
            t=15,
            pad=5
        )
    )
    return fig

@app.callback(Output('gas_comp_chart', 'figure'),
    Input('botao_teste', 'n_clicks'))
def gas_comp(n_clicks):

    while simulation.simulation_status == 0:
        time.sleep(.1)

    variables = ['S_gas_ch4', 'S_gas_co2', 'S_gas_h2', 'h2o']
    names = []
    vals = []
    colors = []
    for variable in variables:
        var_data = simulation.data[variable]
        name = var_data.name
        val = var_data.values[-1]
        color = var_data.color
        names.append(name)
        vals.append(val)
        colors.append(color)

    data = [go.Bar(name=name, x=[val * 100], y=[0], marker_color=color,
            orientation='h', text=[f'{round(val * 100, 1)}%']) 
            for name, val, color in zip(names, vals, colors)]

    fig = go.Figure(data=data)
    fig.update_layout(
        title='Composição do Biogás (%)',
        barmode='stack',
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        legend=dict(
            orientation='h',
            yanchor='top',
            y=-0.1,
            xanchor='left',
            x=0
        ),
        paper_bgcolor=color_p['grey1'],
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(
            l=15,
            r=15,
            b=10,
            t=40,
            pad=5
        ),
        height=200
        )
    return fig

@app.callback(Output('dqo_bar', 'figure'),
    Input('botao_teste', 'n_clicks'))
def gas_comp(n_clicks):
    while simulation.simulation_status == 0:
        time.sleep(.1)

    feed_composition = simulation.feed_composition
    feed_dqo = sum(feed_composition[:22])

    data = simulation.data
    final_dqo = 0
    for variable in data.keys():
        vanilla = data[variable].vanilla
        uom = data[variable].unit
        sub_cat = data[variable].subcategory
        if vanilla and uom == 'kg COD / m-3' and sub_cat != 'Ácidos Desprotonados':
            val = data[variable].values[-1]
            final_dqo += val

    labels = ['Concentração de DQO na Saída', 'Concentração de DQO na Alimentação']
    vals = [final_dqo, feed_dqo]
    text = [f'{label}: {round(val,2)} kg DQO/m³' for label, val in zip(labels, vals)]
    colors = ['#656d4a', '#414833']
    fig = go.Figure(go.Bar(
        x=vals, y=labels,
        orientation='h', text=text,
        marker_color=colors
        ))
    fig.update_layout(
        title='Concentração de DQO',
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        paper_bgcolor=color_p['grey1'],
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(
            l=15,
            r=15,
            b=15,
            t=40,
            pad=5
        ),
        height=200
    )

    return fig
    


# Time Series Chart
@app.callback(Output('time_series', 'figure'),
    [Input('first_axis', 'value'),
    Input('second_axis', 'value')])
def plot_time_series(variable_1, variable_2):

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

    fig.update_layout(
        height=400,
        hovermode='x unified',
        margin=dict(
            l=15,
            r=15,
            b=15,
            t=15,
            pad=5
        )
    )
    return fig
# Area Chart

@app.callback(Output('area_chart', 'figure'),
    Input('area_chart_group', 'value'))
def plot_area_chart(group):

    while simulation.simulation_status == 0:
        time.sleep(.1)

    fig = go.Figure()

    variables_to_plot = []
    colors_to_plot = []
    for variable in simulation.data.keys():

        variable_group = simulation.data[variable].category
        variable_sub_group = simulation.data[variable].subcategory
        variable_color = simulation.data[variable].color

        if variable_group == group:
            variables_to_plot.append(variable)
            colors_to_plot.append(variable_color)
        elif variable_sub_group == group:
            variables_to_plot.append(variable)
            colors_to_plot.append(variable_color)
        
    t = simulation.t
    t = [round(t_current, 1) for t_current in t]

    for variable, color in zip(variables_to_plot, colors_to_plot):
        fig.add_trace(go.Scatter(
            x=t, y=simulation.data[variable].values,
            text=simulation.data[variable].name,
            mode='lines', stackgroup='one',
            line_color=color,
            groupnorm='percent', name=simulation.data[variable].name,
            line=dict(
                width=0.5
            )))

    fig.update_layout(
        height=400,
        showlegend=True,
        hovermode='x unified',
        xaxis_type='category',
        xaxis=dict(
          tickmode='linear',
          tick0=0,
          dtick=100,
          title='Dias'
        ),
        yaxis=dict(
            type='linear',
            range=[1, 100],
            ticksuffix='%'),
        margin=dict(
            l=15,
            r=15,
            b=15,
            t=15,
            pad=0
        )
        )
    return fig

# Dropdowns
@app.callback([Output('first_axis', 'options'),
    Output('second_axis', 'options'),
    Output('area_chart_group', 'options')],
    Input('botao_teste_2', 'n_clicks'))
def populate_dropdown(n_clicks):

    options_variables = []
    options_groups_list = []
    options_groups = []

    while simulation.simulation_status == 0:
        time.sleep(.1)

    for variable in simulation.data.keys():
        # List of variable - To be used with dropdown for line chart
        options_variables.append(
            {
                'label': simulation.data[variable].name,
                'value': variable
            }
        )

        # List of gorups - to be used with area chart graph
        group = simulation.data[variable].category
        sub_group = simulation.data[variable].subcategory
        options_groups_list.extend([group, sub_group])


    options_groups_list = list(set(options_groups_list)) # Get rid of duplicates
    options_groups_list = list(filter(None.__ne__, options_groups_list)) # Removing None

    groups_to_remove = [
        'Ácidos Protonados',
        'Ionização Ácida',
        'Ácidos Desprotonados',
        'Inertes'
    ]
    for group in groups_to_remove:
        options_groups_list.remove(group)


    for group in options_groups_list:
        options_groups.append(
            {
                'label': group,
                'value': group
            }
        )

    return options_variables, options_variables, options_groups

    
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

    generator_efficiency = generator_efficiency * 0.01
    simulation.calculate_financial_value(energy_price=energy_price, generator_efficiency=generator_efficiency)
    monthly_energy = round(simulation.monthly_energy,0)
    monthly_savings = round(simulation.monthly_savings, 2)
    T_index = simulation.data['q_metane'].find_steady_state()
    steady_state_finder =round(simulation.t[T_index])
    return f'• {monthly_energy} kWh gerados por mês • Economia de R${monthly_savings} ao mês • Estado estacionário em {steady_state_finder} dias'
#endregion

#Correlation page callbacks
@app.callback(Output('correlation_target', 'options'),
    Input('dummy_corr', 'n_clicks'))
def goto_correlation_page(n_clicks):

    while simulation.simulation_status == 0:
        time.sleep(.1)

    simulation.diff()
    options_variables = []

    for variable in simulation.data.keys():
        # List of variable - To be used with dropdown for line chart
        if simulation.data[variable].vanilla:
            options_variables.append(
                {
                    'label': simulation.data[variable].name,
                    'value': variable
                }
            )

    return options_variables
    
@app.callback(Output('correlation_heatmap', 'figure'),
    Input('correlation_target', 'value'))
def plot_heatmap(variable):

    while simulation.simulation_status == 0:
        time.sleep(.1)

    # Calculating the derivative for all the vanilla variables
    simulation.diff()

    names = []
    corr_vals = []
    # This is the variable that the correlation will be calculated against
    target_diff = simulation.data[variable].derivative

    for var in simulation.data:

        if var != variable and simulation.data[var].vanilla:
            name = simulation.data[var].name
            var_diff = simulation.data[var].derivative
            corr_index = stats.pearsonr(target_diff, var_diff)
            names.append(name)
            corr_vals.append(corr_index[0])

    sorted_names = [name for val, name in sorted(zip(corr_vals, names))]

    corr_vals = sorted(corr_vals)
    # Need to add all the z values inside a list for the plot to work
    corr_vals = [[val] for val in corr_vals]

    data = go.Heatmap(
        z=corr_vals,
        x=[0],
        y=sorted_names,
        ygap=1,
        colorscale=[
            [0, color_p['4green']],
            [.5, color_p['grey2']],
            [1, color_p['4purple']]
        ],
        hovertemplate='Variável: %{y}<br> Índice de Correlação de Pearson: %{z}' +
                    '<extra></extra>'
    )
    layout = go.Layout(
        height=900,
        width=500,
        xaxis=dict(visible=False)
        )

    fig = go.Figure(data=data, layout=layout)

    return fig

@app.callback([Output('correlation_time_series', 'figure'),
    Output('correlation_scatter', 'figure')],
    [Input('correlation_heatmap', 'clickData'),
    Input('correlation_target', 'value')])
def test_clickData(clickData, variable_1):

    if clickData is None:
        data = go.Scatter(x=[0],y=[0])
        layout=go.Layout(title='Clique em alguma variável no gráfico ao lado')
        fig = go.Figure(data=data,layout=layout)
        return fig, fig
    else:
        variable_2_name = clickData['points'][0]['y']
        for variable in simulation.data.keys():
            var_name = simulation.data[variable].name
            if var_name == variable_2_name:
                variable_2 = variable
                break

    # We will end the chart when steady is achieved to improve visibility of relevant events
    t = simulation.t        
    steady_state_index_1 = simulation.data[variable_1].find_steady_state()

    steady_state_index_2 = simulation.data[variable_2].find_steady_state()
    steady_vals = list(filter(None.__ne__, [steady_state_index_1, steady_state_index_2]))
    steady_time_index = max(steady_vals)
    
    fig = make_subplots(specs=[[{'secondary_y': True}]])
    
    t_plot = t[1:steady_time_index]

    for variable, axis in zip([variable_1, variable_2],[False, True]):
        variable_data = simulation.data[variable]
        y = variable_data.values
        variable_name = variable_data.name
        unit_of_measure = variable_data.unit
        color = variable_data.color

        derivative = variable_data.derivative

        fig.add_trace(
            go.Scatter(
                x=t_plot, y=derivative, 
                name= 'Derivada para: ' + variable_name, marker = dict(color=color),
                mode='lines', line = dict(dash='dash')
                ),
            secondary_y=axis
        )
        fig.update_yaxes(title_text= f'{variable_name} ({unit_of_measure} / dias)', secondary_y=axis)
    fig.update_xaxes(title_text='Tempo (dias)')

    fig.update_layout(
        height=400,
        hovermode='x unified',
        margin=dict(
            l=15,
            r=15,
            b=15,
            t=15,
            pad=5
        )
    )

    fig_scatter = go.Figure(data=go.Scatter(
        x=simulation.data[variable_1].derivative,
        y=simulation.data[variable_2].derivative,
        mode='markers'
    ))

    return fig, fig_scatter

# Callback do collapse
@app.callback(
    Output("collapse_advanced_options", "is_open"),
    [Input("advanced_options_button", "n_clicks")],
    [State("collapse_advanced_options", "is_open")],
)

def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
######

if __name__ == '__main__':
    app.run_server(debug=True)

