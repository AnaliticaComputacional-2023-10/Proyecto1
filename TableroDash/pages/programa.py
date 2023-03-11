from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation
from app import app
import dash_daq as daq

programa_layout = html.Div(children=[
    navigation.navbar,
    html.Br(),
    html.H1(children = "Programa de Predicción de Enfermedades Cardíacas",
            style={'textAlign': 'center'}),
    html.Div([
    daq.BooleanSwitch(id='our-boolean-switch', on=False),
    html.Div(id='boolean-switch-result')
    ])
])

@app.callback(
    Output('boolean-switch-result', 'children'),
    Input('our-boolean-switch', 'on')
)
def update_output(on):
    return f'The switch is {on}.'