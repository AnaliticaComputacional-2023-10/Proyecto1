from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation
import dash_bootstrap_components as dbc

inicio_layout = html.Div(children=[
    navigation.navbar,
    html.Br(),
    html.H1(children = "Bienvenido al Programa de Predicción de Enfermedades Cardíacas",
            style={'textAlign': 'center'}),
    html.Br(),
    html.Div(children='Está aplicación ayuda a predecir enfermedades cardíacas por medio de variables explicativas', style={
        'textAlign': 'center'
    }),
    html.Br(),
    html.Div(children=[
        dbc.Button("Instrucciones", size="lg", id="inicio_instrucciones",href="/instrucciones",
                   style={'margin-left': '620px',
                            'margin-bottom': '10px',
                            'verticalAlign': 'middle'})
        ]),
    html.Br(),
    html.Div(children=[
        dbc.Button("Programa", size="lg", id="inicio_programa",href="/programa",
                   style={'margin-left': '635px',
                            'margin-bottom': '10px',
                            'verticalAlign': 'middle'})
        ]),
    html.Div(children='Está aplicación ha sido creada por Santiago González y Juliana Cárdenas', style={
        'textAlign': 'center'
    }),
    html.Br()
])