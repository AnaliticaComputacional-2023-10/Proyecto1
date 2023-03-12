from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation
from app import app
import dash_bootstrap_components as dbc
import dash_daq as daq

programa_layout = html.Div(children=[
    navigation.navbar,
    html.Br(),
    html.H1(children = "Programa de Predicción de Enfermedades Cardíacas",
            style={'textAlign': 'center'}),
    html.Br(),
    #Columnas
    html.Div(
    [dbc.Row(
            [
                dbc.Col(
                    html.Div("One of three columns")
                    ),
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
            ]
        ),
    ]
)

])
