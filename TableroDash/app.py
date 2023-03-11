import dash
import dash_html_components as html
import dash_core_components as dcc #Para los inputs
from dash.dependencies import Input, Output #callback

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    #html.H1(children = "Bienvenido al Programa de Predicción de Enfermedades Cardíacas"),
    dcc.Location(id="url",refresh=False),
    #dcc.Link('Inicio',href="/"),
    #html.Br(),
    #dcc.Link('Instrucciones',href="/instrucciones"),
    #html.Br(),
    #dcc.Link('Programa',href="/programa"),
    html.Div(id="output-div")
])

inicio_layout = html.Div(children=[
    html.H1(children = "Bienvenido al Programa de Predicción de Enfermedades Cardíacas"),
    dcc.Link('Inicio',href="/"),
    html.Br(),
    dcc.Link('Instrucciones',href="/instrucciones"),
    html.Br(),
    dcc.Link('Programa',href="/programa")
])

instrucciones_layout = html.Div(children=[
    html.H1(children = "Aca encontrara las instrucciones para utilizar la aplicación"),
    dcc.Link('Inicio',href="/"),
    dcc.Link('Programa',href="/programa")
])

programa_layout =html.Div(children=[
    html.H1(children = "Aca encontrara la aplicación"),
    dcc.Link('Inicio',href="/"),
    dcc.Link('Instrucciones',href="/instrucciones")
])

@app.callback(Output(component_id='output-div', component_property='children'),
              [Input(component_id='url', component_property='pathname')])
def update_output_div(pathname):
    if pathname == '/instrucciones':
        return instrucciones_layout
    elif pathname == '/programa':
        return programa_layout
    else:
        return inicio_layout
    #output_val = "Output: {}".format(pathname)
    #return output_val

if __name__ == "__main__":
    app.run_server(debug=True)
