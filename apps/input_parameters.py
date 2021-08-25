#Importing Libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pathlib
# Importing support files
from app import app
PATH = pathlib.Path(__file__).parent
# Connecting files (Include data paths below)

app = dash.Dash(__name__)

# Data manipulation (Import and clean data from support files)
DQO = 125 # kg/DQO parameters
pH = 7 
massa_dia = 3 #kg/m³
V_digestor_liq = 20 # m3
V_digestor_gas = 20 # m³

# Layout

layout = html.div([
    html.H1('Insira os dados solicitados para a simulação: ', style={"textAlign": "center"}),

    html.div([

    ])
])
# Callbacks

# Run Server

if __name__ == '__main__':
    app.run_server(debug=True)


