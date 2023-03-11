from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation

programa_layout =html.Div(children=[
    navigation.navbar,
    html.H1(children = "Aca encontrara la aplicación")
])