from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation
from app import app

options = [
    {'label': 'Variable 1', 'value': 'value_1'},
    {'label': 'Variable 2', 'value': 'value_2'},
    {'label': 'Variable 3', 'value': 'value_3'}
]

instrucciones_layout = html.Div(children=[
    navigation.navbar,
    html.Br(),
    html.H1(children = "Instrucciones para usar el Programa",
            style={'textAlign': 'center'}),
    html.Br(),
    #Selección de variables
    html.Div([
        html.Label('Seleccione una variable:'),
        dcc.Dropdown(
            id='variable-dropdown',
            options=options,
            value=options[0]['value']
        )
    ], style={'width': '50%', 'display': 'inline-block','margin-right':'20px 0'}),
    html.Div([
        html.Label('Resultado:'),
        html.Div(id='output')
    ], style={'width': '50%', 'display': 'inline-block','margin-left':'20px 0'}),
])

@app.callback(Output('output', 'children'), [Input('variable-dropdown', 'value')])
def update_output(value):
    # Aquí es donde se realiza el cálculo correspondiente a la variable seleccionada
    if value == 'value_1':
        result = 'Resultado de la variable 1'
    elif value == 'value_2':
        result = 'Resultado de la variable 2'
    elif value == 'value_3':
        result = 'Resultado de la variable 3'
    else:
        result = 'Selecciona una variable'
    return result