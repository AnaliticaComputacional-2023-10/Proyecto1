from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation
from app import app
import dash_bootstrap_components as dbc
import dash_daq as daq
import pandas as pd

programa_layout = html.Div(children=[
    navigation.navbar,
    html.Br(),
    html.H1(children = "Programa de Predicción de Enfermedades Cardíacas",
            style={'textAlign': 'center'}),
    html.Br(),

    dbc.Row([
        dbc.Col([html.Div("Información del Paciente",
                          style={'font-weight': 'bold', 'font-size': 20}),
            dbc.Row([html.Div("Datos demográficos del paciente",
                              style={'font-weight': 'bold', 'font-size': 16, 'padding': '10px 25px'})]),
            dbc.Row([
                dbc.Col(html.Div([
                    html.Label('Edad del paciente (en años): '),
                    dcc.Input(
                        type="number",
                        debounce=True,
                        value='',
                        id='age'
                    )
                ]), width={"size": 3}),
                dbc.Col(html.Div([
                    html.Label('Sexo: '),
                    dcc.Dropdown(
                        options=[
                            {'label': 'Hombre', 'value': '1'},
                            {'label': 'Mujer', 'value': '0'}
                        ],
                        value='',
                        id='sex_male'
                    )
                ]), width={"size": 3},style={'margin-left':'50px'}),
            ], style={'padding': '10px 25px'}),
            dbc.Row([html.Div("Salud del paciente",
                              style={'font-weight': 'bold', 'font-size': 16, 'padding': '10px 25px'})]),
            dbc.Row([
                dbc.Col(html.Div([
                    html.Label('Presión arterial (mmHg): '),
                    dcc.Input(
                        type="number",
                        debounce=True,
                        value='',
                        id='resting_bp'
                    )
                ]), width={"size": 3}, style={'padding': '10px 10px'}),
                dbc.Col(html.Div([
                    html.Label('Frecuencia cardíaca máxima (bpm): '),
                    dcc.Input(
                        type="number",
                        debounce=True,
                        value='',
                        id='maximum_hr'
                    )
                ]), width={"size": 3}, style={'padding': '10px 50px'}),
                dbc.Col(html.Div([
                    html.Label('Colesterol sérico (mg/dL): '),
                    dcc.Input(
                        type="number",
                        debounce=True,
                        value='',
                        id='serum_cholesterol'
                    )
                ]), width={"size": 3}, style={'padding': '10px 90px'}),
                dbc.Col(html.Div([
                    html.Label('Azúcar en sangre en ayunas: '),
                    dcc.Input(
                        type="number",
                        debounce=True,
                        value='',
                        id='fasting_blood_sugar'
                    )
                ]), width={"size": 3}, style={'padding': '10px 10px'}),
            ], style={'padding': '10px 25px'}),
            dbc.Row([
                dbc.Col(html.Div([
                    html.Label('Tipo de dolor en el pecho: '),
                    dcc.Dropdown(
                        options=[
                            {'label': 'Angina típica', 'value': '1'},
                            {'label': 'Angina atípica', 'value': '2'},
                            {'label': 'No anginoso', 'value': '3'},
                            {'label': 'Asintomático', 'value': '4'}
                        ],
                        value='',
                        id='chest_pain_type'
                    )
                ]), width={"size": 3}),
                dbc.Col(html.Div([
                    html.Label('Angina inducida por el ejercicio: '),
                    dcc.Dropdown(
                        options=[
                            {'label': 'Si', 'value': '1'},
                            {'label': 'No', 'value': '0'}
                        ],
                        value='',
                        id='exercise_induced_angina_yes'
                    )
                ]), width={"size": 3}),
            ], style={'padding': '10px 25px'}),
            dbc.Row([html.Div("Resultados ECG",
                              style={'font-weight': 'bold', 'font-size': 16, 'padding': '10px 25px'})]),
            dbc.Row([
                dbc.Col(html.Div([
                    html.Label('Resultados ECG en reposo: '),
                    dcc.Dropdown(
                        options=[
                            {'label': 'Normales', 'value': '0'},
                            {'label': 'No normales', 'value': '1'}
                        ],
                        value='',
                        id='resting_ecg_not_normal'
                    )
                ]), width={"size": 3}),
                dbc.Col(html.Div([
                    html.Label('Depresión del ST: '),
                    dcc.Input(
                        type="number",
                        debounce=True,
                        value='',
                        id='ST_depression_exercise_vs_rest'
                    )
                ]), width={"size": 3}),
                dbc.Col(html.Div([
                    html.Label('Pendiente del segmento ST: '),
                    dcc.Dropdown(
                        options=[
                            {'label': 'Ascendente', 'value': '1'},
                            {'label': 'Plana o descendente', 'value': '0'}
                        ],
                        value='',
                        id='peak_exercise_ST_segment_slope_upsloping'
                    )
                ]), width={"size": 3},style={'margin-left':'50px'}),
            ], style={'padding': '10px 25px'}),
            dbc.Row([html.Div("Resultados de la prueba de esfuerzo nuclear.",
                              style={'font-weight': 'bold', 'font-size': 16, 'padding': '10px 25px'})]),
            dbc.Row([
                dbc.Col(html.Div([
                    html.Label('Blood flow: '),
                    dcc.Dropdown(
                        options=[
                            {'label': 'Normal', 'value': '1'},
                            {'label': 'Defectuosa', 'value': '0'}
                        ],
                        value='',
                        id='thallium_stress_test_bf_normal'
                    )
                ]), width={"size": 3}),
                dbc.Col(html.Div([
                    html.Label('Affected vessels: '),
                    dcc.Input(
                        type="number",
                        debounce=True,
                        value='',
                        id='num_affected_major_vessels'
                    )
                ]), width={"size": 3}),
            ], style={'padding': '10px 25px'}),
        ], style={'padding': '10px 25px'}
        ),

        # Columna de la derecha con la información del riesgo previsto de enfermedad cardíaca
        dbc.Col([
            html.Div("Riesgo previsto de enfermedad cardiaca",
                          style={'font-weight': 'bold', 'font-size': 20}),
            html.Div(id='data_patient')
            ],
            style={'padding': '10px 25px'}
        ),
    ]),
    html.Br(),
    html.Div(children=[
            dbc.Button(
                    "Predecir Modelo",
                    id="collapse-button",
                    className="mb-3",
                    color="primary",
                )],
        style={'margin-bottom': '10px',
              'display': 'flex',
              'justify-content': 'center',
              'margin-right':'800px'})
    ]
)
