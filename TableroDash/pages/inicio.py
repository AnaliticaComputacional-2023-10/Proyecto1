from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation

inicio_layout = html.Div(children=[
    navigation.navbar,
    html.H1(children = "Bienvenido al Programa de Predicción de Enfermedades Cardíacas")
])