import dash_html_components as html
import dash_core_components as dcc #Para los inputs
from dash.dependencies import Input, Output #callback

programa_layout =html.Div(children=[
    html.H1(children = "Aca encontrara la aplicación"),
    dcc.Link('Inicio',href="/"),
    html.Br(),
    dcc.Link('Instrucciones',href="/instrucciones")
])