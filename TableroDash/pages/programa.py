from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation
from app import app

programa_layout = html.Div(children=[
    navigation.navbar,
    html.Br(),
    html.H1(children = "Programa de Predicción de Enfermedades Cardíacas",
            style={'textAlign': 'center'}),
    html.Br(),
    #Columnas
    html.Div([
    html.Div(children=[
        html.Label('Dropdown')
    ], style={'padding': 10, 'flex': 1}),

    html.Div(children=[
        html.Label('Checkboxes'),
        html.Br(),
        html.Label('Slider'),
        dcc.Slider(
            min=0,
            max=9,
            marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 6)},
            value=5,
        ),
    ], style={'padding': 10, 'flex': 1})
], style={'display': 'flex', 'flex-direction': 'row'})
])