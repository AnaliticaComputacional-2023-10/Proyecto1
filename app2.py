# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Creamos una instancia de la aplicación
app = dash.Dash(__name__)

columns = {
    "age": {'meaning': 'age in years',
            'num': 3},
    "sex": {'meaning': 'sex (1 = male; 0 = female)',
            'num': 4},
    "cp": {'meaning': 'chest pain type 1: typical angina; 2: atypical angina; 3: non-anginal pain; 4: asymptomatic',
           'num': 9},
    "trestbps": {'meaning': 'resting blood pressure (in mm Hg on admission to the hospital)',
                 'num': 10},
    "chol": {'meaning': 'serum cholestoral in mg/dl',
             'num': 12},
    "fbs": {'meaning': '(fasting blood sugar > 120 mg/dl)  (1 = true; 0 = false)',
            'num': 16},
    "restecg": {'meaning': 'resting electrocardiographic results 0: normal; 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV); 2: showing probable or definite left ventricular hypertrophy by Estes criteria',
                'num': 19},
    "thalach": {'meaning': 'maximum heart rate achieved',
                'num': 32},
    "exang": {'meaning': 'exercise induced angina (1 = yes; 0 = no)',
              'num': 38},
    "oldpeak": {'meaning': 'ST depression induced by exercise relative to rest',
                'num': 40},
    "slope": {'meaning': 'the slope of the peak exercise ST segment 1: upsloping; 2: flat; 3: downsloping',
              'num': 41},
    "ca": {'meaning': 'number of major vessels (0-3) colored by flourosopy',
           'num': 44},
    "thal": {'meaning': '3 = normal; 6 = fixed defect; 7 = reversable defect',
             'num': 51},
    "num": {'meaning': 'diagnosis of heart disease (angiographic disease status) 0: < 50% diameter narrowing; 1: > 50% diameter narrowing',
            'num': 58},
}

# Cargamos los datos para las gráficas
df = pd.read_csv("Data/processed.cleveland.data", names=[i for i in columns.keys()])

df.age = df.age.astype(int)
df.sex = df.sex.astype(int)
df.cp = df.cp.astype(int)
df.trestbps = df.trestbps.astype(int)
df.chol = df.chol.astype(int)
df.fbs = df.fbs.astype(int)
df.restecg = df.restecg.astype(int)
df.thalach = df.thalach.astype(int)
df.exang = df.exang.astype(int)
df.slope = df.slope.astype(int)

# Definimos el layout para la página de instrucciones
layout_instrucciones = html.Div([
    html.H1('Instrucciones'),
    html.P('Estas son las instrucciones para utilizar el dashboard.'),
    html.P('Primero, selecciona una opción en el menú de navegación.'),
    html.P('Después, sigue las instrucciones en cada página para interactuar con las visualizaciones.'),
])

# Definimos el layout para la página de gráficas
layout_graficas = html.Div([
    html.H1('Gráficas'),
    html.P('En esta página encontrarás algunas visualizaciones de los datos.'),
    dcc.Graph(
        id='grafica-1',
        figure=px.scatter(df, x='age', y='sex')
    ),
    dcc.Graph(
        id='grafica-2',
        figure=px.line(df, x='age', y='sex')
    ),
])

# Definimos el layout para la página de inicio
layout_inicio = html.Div([
    html.H1('Predicción de Enfermedades Cardiacas'),
    html.P('Bienvenido al dashboard.'),
    html.P('Por favor, selecciona una opción en el menú de navegación para comenzar.'),
])

# Definimos el layout para el contenido de la página
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Nav([
        dcc.Link('Inicio', href='/'),
        dcc.Link('Instrucciones', href='/instrucciones'),
        dcc.Link('Predicción', href='/graficas'),
    ]),
    html.Div(id='page-content')
])

# Definimos el callback para actualizar el contenido de la página
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/instrucciones':
        return layout_instrucciones
    elif pathname == '/graficas':
        return layout_graficas
    else:
        return layout_inicio

if __name__ == '__main__':
    app.run_server(debug=True)