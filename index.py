import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

from apps import dashboard, input_parameters

app.layout = html.Div ([
    dcc.Link(html.Button('Inputs'), href='apps/input_parameters'),
    dcc.Link(html.Button('Outputs'), href='apps/dashboard'),

])