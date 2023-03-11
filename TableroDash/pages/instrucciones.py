from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation

instrucciones_layout = html.Div(children=[
    navigation.navbar,
    html.H1(children = "Aca encontrara las instrucciones para utilizar la aplicación")
])