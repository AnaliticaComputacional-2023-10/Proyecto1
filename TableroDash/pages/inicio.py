import dash_html_components as html
import dash_core_components as dcc #Para los inputs
from dash.dependencies import Input, Output #callback

inicio_layout = html.Div(children=[
    html.H1(children = "Bienvenido al Programa de Predicción de Enfermedades Cardíacas"),
    dcc.Link('Inicio',href="/"),
    html.Br(),
    dcc.Link('Instrucciones',href="/instrucciones"),
    html.Br(),
    dcc.Link('Programa',href="/programa")
])