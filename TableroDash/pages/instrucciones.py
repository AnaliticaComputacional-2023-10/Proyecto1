from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation

instrucciones_layout = html.Div(children=[
    navigation.navbar,
    html.Br(),
    html.H1(children = "Instrucciones para usar el Programa",
            style={'textAlign': 'center'})
])