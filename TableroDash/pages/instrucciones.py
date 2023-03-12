from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation
from app import app
import dash_bootstrap_components as dbc

options = [
    {'label': 'Edad', 'value': 'age'},
    {'label': 'Sexo', 'value': 'sex'},
    {'label': 'Tipo de dolor en el pecho', 'value': 'cp'},
    {'label': 'Presión arterial en reposo', 'value': 'trestbps'},
    {'label': 'Colesterol sérico', 'value': 'chol'},
    {'label': 'Azúcar en sangre en ayunas', 'value': 'fbs'},
    {'label': 'Resultados electrocardiográficos en reposo', 'value': 'restecg'},
    {'label': 'Frecuencia cardíaca máxima alcanzada', 'value': 'thalach'},
    {'label': 'Angina inducida por el ejercicio', 'value': 'exang'},
    {'label': 'Depresión del ST del pico anterior inducida por el ejercicio en relación con el reposo', 'value': 'oldpeak'},
    {'label': 'Pendiente del segmento ST de ejercicio máximo', 'value': 'slope'},
    {'label': 'Número de vasos principales coloreados por fluoroscopia', 'value': 'ca'},
    {'label': 'Talasemia', 'value': 'thal'}
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
            value=''
        )
    ], style={'width': '50%', 'display': 'inline-block','margin-right':'20px 0'}),
    html.Div([
        html.Label('Que debe hacer en el programa:'),
        html.Div(id='output')
    ], style={'width': '50%', 'display': 'inline-block','margin-left':'20px 0'}),
    html.Br(),
    #Botones para ir de la pagina de inicio a las instrucciones y programa
    html.Br(),
    html.Div(children=[
        html.Div(children=[
            dbc.Button("Programa", size="lg", id="inicio_programa", href="/programa",
                       style={'margin-left': '10px', 'verticalAlign': 'middle'})],
            style={'display': 'inline-flex'})],
        style={'margin-bottom': '10px',
              'display': 'flex',
              'justify-content': 'center'})
])

@app.callback(Output('output', 'children'), [Input('variable-dropdown', 'value')])
def update_output(value):
    # Aquí es donde se realiza el cálculo correspondiente a la variable seleccionada
    if value == 'age':
        result = 'Resultado de la edad'
    elif value == 'sex':
        result = 'Resultado del sexo'
    elif value == 'cp':
        result = 'Resultado del tipo de dolor en el pecho'
    elif value == 'trestbps':
        result = 'Resultado de la presión arterial en reposo'
    elif value == 'chol':
        result = 'Resultado del colesterol sérico'
    elif value == 'fbs':
        result = 'Resultado del azúcar en sangre en ayunas'
    elif value == 'restecg':
        result = 'Resultado de los resultados electrocardiográficos en reposo'
    elif value == 'thalach':
        result = 'Resultado de la frecuencia cardíaca máxima alcanzada'
    elif value == 'exang':
        result = 'Resultado de la angina inducida por el ejercicio'
    elif value == 'oldpeak':
        result = 'Resultado de la depresión del ST del pico anterior inducida por el ejercicio en relación con el reposo'
    elif value == 'slope':
        result = 'Resultado de la pendiente del segmento ST de ejercicio máximo'
    elif value == 'ca':
        result = 'Resultado del número de vasos principales coloreados por fluoroscopia'
    elif value == 'thal':
        result = 'Resultado de la talasemia'
    else:
        result = 'Selecciona una variable'
    return result
