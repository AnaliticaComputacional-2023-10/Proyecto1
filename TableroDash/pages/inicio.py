from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation
import dash_bootstrap_components as dbc

texto = '''Las enfermedades cardíacas son una de las principales causas de muerte en todo el mundo.
Estas enfermedades afectan al corazón y al sistema circulatorio, lo que puede llevar a complicaciones
graves, como ataques cardíacos y accidentes cerebrovasculares.

El siguiente programa ha sido desarrollado como apoyo a médicos en el proceso de evaluación de
pacientes para detectar si una persona tiene o no una enfermedad cardíaca y la toma de decisiones
asociada como solicitud de exámenes, chequeos y otros procedimientos.'''

texto2 = '''Este programa se ha desarrollado mediante la exploración de datos y el modelado con
redes bayesianas, con el fin de descubrir la relación entre 14 atributos relevantes en la base
de datos de enfermedades cardíacas de Cleveland. Los datos se recopilaron del repositorio de la
Universidad de California en Irvine.'''

texto3 = 'Aplicación creada por Santiago González y Juliana Cárdenas'

inicio_layout = html.Div(children=[
    navigation.navbar,
    html.Br(),
    #Titulo
    html.H1(children = "Bienvenido al Programa de Predicción de Enfermedades Cardíacas",
            style={'textAlign': 'center'}),
    html.Br(),
    #Parrafo inicial
    html.Div(html.Pre(texto, style={'text-align': 'center','padding':'1px'})),
    html.Br(),
    #Imagen y texto
    html.Div(children=[
        html.Img(src='/assets/img1.png', style={'height': '10%', 'width': '10%','margin-right':'10px'}),
        html.Div(children=[
            html.Pre(texto2, style={'text-align': 'center','padding':'1px'})
        ], style={'margin-left': '10px'})
    ],
    style={'display': 'flex',
           'align-items': 'center',
           'justify-content': 'flex-start',
           'margin-left': '280px'}),
    html.Br(),
    #Botones para ir de la pagina de inicio a las instrucciones y programa
    html.Div(children=[
        html.Div(children=[
            dbc.Button("Instrucciones", size="lg", id="inicio_instrucciones", href="/instrucciones",
                       style={'margin-right': '10px', 'verticalAlign': 'middle'})],
            style={'display': 'inline-flex'}),
        html.Div(children=[
            dbc.Button("Programa", size="lg", id="inicio_programa", href="/programa",
                       style={'margin-left': '10px', 'verticalAlign': 'middle'})],
            style={'display': 'inline-flex'})],
        style={'margin-bottom': '10px',
              'display': 'flex',
              'justify-content': 'center'}),
    html.Br(),
    html.Div(html.Pre(texto3, style={'text-align': 'center'}))
])
