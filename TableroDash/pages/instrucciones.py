from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation
from app import app
import dash_bootstrap_components as dbc

tipo = '''Ingrese el tipo de dolor que
presenta el paciente.

Angina típica: Dolor o molestia
en el pecho que puede sentirse
como una presión, opresión,
quemazón o dolor agudo en el
centro del pecho. La duración
del dolor es generalmente breve
y dura entre 1 y 5 minutos. El
dolor se desencadena por una
actividad física o emocional
específica. El dolor mejora con
el reposo o la disminución de
la actividad.

Angina atípica: Dolor o molestia
que puede sentirse como una
sensación de ardor, opresión o
presión en el pecho. El dolor no
esta solamente localizado en el
centro del pecho, sino en otras
áreas, como la mandíbula, el
cuello, la espalda, los brazos
o el estómago. El dolor dura más
de 5 minutos, es constante o
intermitente, y no está relacio-
nado con la actividad física.

No anginoso: El dolor se siente
en diferentes áreas del pecho,
como en el lado izquierdo,
derecho o en el centro del pecho.
El dolor puede sentirse como una
sensación de presión hasta un
dolor punzante.La duración
del dolor es de pocos segundos
hasta 2 minutos.No está relacio-
nado con la actividad física.

Asintomático: No presenta dolor
en el pecho.
'''

resultados = ''' fiusbfidvnnvsd
'''

instrucciones_layout = html.Div(children=[
    navigation.navbar,
    html.Br(),
    html.H1(children = "Instrucciones para usar el Programa",
            style={'textAlign': 'center'}),
    html.Br(),

    #Primera fila

    html.Div(
        dbc.Row(
            [
                #Edad
                dbc.Col(
                    dbc.Card([
                        dbc.CardImg(src='/assets/edad.png',
                                    style={'height': '50%', 'width': '50%','display': 'block', 'margin': 'auto', 'align-self': 'center'},
                                    top=True),
                        dbc.CardBody([
                            dbc.Accordion(
                                dbc.AccordionItem([
                                html.P("Ingrese la edad del paciente en años.")],
                            title="Edad"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "23rem"}, color="primary", outline=True),
                    className="mb-4",
                ),
                #Sexo
                dbc.Col(
                    dbc.Card([
                        dbc.CardImg(src='/assets/sexo.png',
                                    style={'height': '50%', 'width': '50%','display': 'block', 'margin': 'auto', 'align-self': 'center'},
                                    top=True),
                        dbc.CardBody([
                            dbc.Accordion(
                                dbc.AccordionItem([
                                html.P("Ingrese el sexo del paciente(Hombre o Mujer).")],
                            title="Sexo"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "23rem"}, color="primary", outline=True),
                    className="mb-4"
                ),
                #Tipo de dolor en el pecho
                dbc.Col(
                    dbc.Card([
                        dbc.CardImg(src='/assets/dolor.png',
                                    style={'height': '50%', 'width': '50%','display': 'block', 'margin': 'auto', 'align-self': 'center'},
                                    top=True),
                        dbc.CardBody([
                            dbc.Accordion(
                                dbc.AccordionItem([
                                html.Pre(tipo)],
                            title="Tipo de dolor en el pecho"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "23rem"}, color="primary", outline=True),
                    className="mb-4"
                ),
            ],
            className="mt-4",
        ),
        style={'display': 'flex',
              'justify-content': 'center'}
    ),

    #Segunda fila

    html.Div(
        dbc.Row(
            [
                #Presión arterial en reposo
                dbc.Col(
                    dbc.Card([
                        dbc.CardImg(src='/assets/presion.png',
                                    style={'height': '50%', 'width': '50%','display': 'block', 'margin': 'auto', 'align-self': 'center'},
                                    top=True),
                        dbc.CardBody([
                            dbc.Accordion(
                                dbc.AccordionItem([
                                html.P("Ingrese la presión arterial del paciente en mmHg.")],
                            title="Presión arterial en reposo"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "23rem"}, color="primary", outline=True),
                    className="mb-4",
                ),
                #Colesterol sérico
                dbc.Col(
                    dbc.Card([
                        dbc.CardImg(src='/assets/colesterol.png',
                                    style={'height': '50%', 'width': '50%','display': 'block', 'margin': 'auto', 'align-self': 'center'},
                                    top=True),
                        dbc.CardBody([
                            dbc.Accordion(
                                dbc.AccordionItem([
                                html.P("Ingrese el colesterol serico del paciente en mg/dl.")],
                            title="Colesterol sérico"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "23rem"}, color="primary", outline=True),
                    className="mb-4"
                ),
                #Azúcar en sangre en ayunas
                dbc.Col(
                    dbc.Card([
                        dbc.CardImg(src='/assets/glucosa.png',
                                    style={'height': '50%', 'width': '50%','display': 'block', 'margin': 'auto', 'align-self': 'center'},
                                    top=True),
                        dbc.CardBody([
                            dbc.Accordion(
                                dbc.AccordionItem([
                                html.P("Ingrese el azúcar en sangre en ayunas del paciente en mg/dl.")],
                            title="Azúcar en sangre en ayunas"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "23rem"}, color="primary", outline=True),
                    className="mb-4"
                ),
            ],
            className="mt-4",
        ),
        style={'display': 'flex',
              'justify-content': 'center'}
    ),

    #Tercera fila

    html.Div(
        dbc.Row(
            [
                #Resultados electrocardiográficos en reposo
                dbc.Col(
                    dbc.Card([
                        dbc.CardImg(src='/assets/electro.png',
                                    style={'height': '50%', 'width': '50%','display': 'block', 'margin': 'auto', 'align-self': 'center'},
                                    top=True),
                        dbc.CardBody([
                            dbc.Accordion(
                                dbc.AccordionItem([
                                html.Pre(resultados)],
                            title="Resultados electrocardiográficos en reposo"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "23rem"}, color="primary", outline=True),
                    className="mb-4",
                ),
                #Frecuencia cardíaca máxima alcanzada
                dbc.Col(
                    dbc.Card([
                        dbc.CardImg(src='/assets/frec.png',
                                    style={'height': '50%', 'width': '50%','display': 'block', 'margin': 'auto', 'align-self': 'center'},
                                    top=True),
                        dbc.CardBody([
                            dbc.Accordion(
                                dbc.AccordionItem([
                                html.P("Frecuencia cardíaca máxima alcanzada por en paciente en bpm")],
                            title="Frecuencia cardíaca máxima alcanzada"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "23rem"}, color="primary", outline=True),
                    className="mb-4"
                ),
                #Angina inducida por el ejercicio
                dbc.Col(
                    dbc.Card([
                        dbc.CardImg(src='/assets/ejercicio.png',
                                    style={'height': '50%', 'width': '50%','display': 'block', 'margin': 'auto', 'align-self': 'center'},
                                    top=True),
                        dbc.CardBody([
                            dbc.Accordion(
                                dbc.AccordionItem([
                                html.P("El dolor en el pecho que presenta el paciente se desencadena por una actividad física")],
                            title="Angina inducida por el ejercicio"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "23rem"}, color="primary", outline=True),
                    className="mb-4"
                ),
            ],
            className="mt-4",
        ),
        style={'display': 'flex',
              'justify-content': 'center'}
    ),

    #Cuarta fila

    html.Div(
        dbc.Row(
            [
                #Depresión del ST del pico anterior inducida por el ejercicio en relación con el reposo
                dbc.Col(
                    dbc.Card([
                        dbc.CardImg(src='/assets/electro2.png',
                                    style={'height': '50%', 'width': '50%','display': 'block', 'margin': 'auto', 'align-self': 'center'},
                                    top=True),
                        dbc.CardBody([
                            dbc.Accordion(
                                dbc.AccordionItem([
                                html.P("This is the content of the first section")],
                            title="Depresión del ST del pico anterior inducida por el ejercicio en relación con el reposo"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "23rem"}, color="primary", outline=True),
                    className="mb-4",
                ),
                #Pendiente del segmento ST de ejercicio máximo
                dbc.Col(
                    dbc.Card([
                        dbc.CardImg(src='/assets/electro3.png',
                                    style={'height': '50%', 'width': '50%','display': 'block', 'margin': 'auto', 'align-self': 'center'},
                                    top=True),
                        dbc.CardBody([
                            dbc.Accordion(
                                dbc.AccordionItem([
                                html.P("This is the content of the first section")],
                            title="Pendiente del segmento ST de ejercicio máximo"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "23rem"}, color="primary", outline=True),
                    className="mb-4"
                ),
                #Número de vasos principales coloreados por fluoroscopia
                dbc.Col(
                    dbc.Card([
                        dbc.CardImg(src='/assets/vasos.png',
                                    style={'height': '50%', 'width': '50%','display': 'block', 'margin': 'auto', 'align-self': 'center'},
                                    top=True),
                        dbc.CardBody([
                            dbc.Accordion(
                                dbc.AccordionItem([
                                html.P("Número de vasos sanguineos coloreados por fluoroscopia que presenta el paciente.")],
                            title="Número de vasos principales coloreados por fluoroscopia"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "23rem"}, color="primary", outline=True),
                    className="mb-4"
                ),
            ],
            className="mt-4",
        ),
        style={'display': 'flex',
              'justify-content': 'center'}
    ),

    #Quinta fila

    html.Div(
        dbc.Row(
            [
                #Talasemia
                dbc.Col(
                    dbc.Card([
                        dbc.CardImg(src='/assets/thal.png',
                                    style={'height': '50%', 'width': '50%','display': 'block', 'margin': 'auto', 'align-self': 'center'},
                                    top=True),
                        dbc.CardBody([
                            dbc.Accordion(
                                dbc.AccordionItem([
                                html.P("This is the content of the first section")],
                            title="Talasemia"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "23rem"}, color="primary", outline=True),
                    className="mb-4",
                ),
            ],
            className="mt-4",
        ),
        style={'display': 'flex',
              'justify-content': 'center'}
    ),

    #Botones para ir de la pagina del programa
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