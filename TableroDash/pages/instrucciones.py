from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation
from app import app
import dash_bootstrap_components as dbc

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
                                html.P("This is the content of the first section")],
                            title="Edad"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "22rem"}, color="primary", outline=True),
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
                                html.P("This is the content of the first section")],
                            title="Sexo"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "22rem"}, color="primary", outline=True),
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
                                html.P("This is the content of the first section")],
                            title="Tipo de dolor en el pecho"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "22rem"}, color="primary", outline=True),
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
                                html.P("This is the content of the first section")],
                            title="Presión arterial en reposo"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "22rem"}, color="primary", outline=True),
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
                                html.P("This is the content of the first section")],
                            title="Colesterol sérico"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "22rem"}, color="primary", outline=True),
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
                                html.P("This is the content of the first section")],
                            title="Azúcar en sangre en ayunas"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "22rem"}, color="primary", outline=True),
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
                                html.P("This is the content of the first section")],
                            title="Resultados electrocardiográficos en reposo"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "22rem"}, color="primary", outline=True),
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
                                html.P("This is the content of the first section")],
                            title="Frecuencia cardíaca máxima alcanzada"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "22rem"}, color="primary", outline=True),
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
                                html.P("This is the content of the first section")],
                            title="Angina inducida por el ejercicio"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "22rem"}, color="primary", outline=True),
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
                    )], style={"width": "22rem"}, color="primary", outline=True),
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
                            title="FPendiente del segmento ST de ejercicio máximo"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "22rem"}, color="primary", outline=True),
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
                                html.P("This is the content of the first section")],
                            title="Número de vasos principales coloreados por fluoroscopia"),
                            start_collapsed=True)
                        ]
                    )], style={"width": "22rem"}, color="primary", outline=True),
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
                    )], style={"width": "22rem"}, color="primary", outline=True),
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