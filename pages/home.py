#Libraries
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

#Own functions
from components.cards.sidecard import sidecard

#from app import app

#Add home to page registry
register_page(__name__, path="/", name="Inicio", title="Home Fusion Center", order=1)

#Define content
content_home=  dbc.Container([

    dbc.Row(html.H4("Herramienta para el ánalisis de reportes", 
        style={'textAlign': 'center', "font-weight":"bold"})),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardImg(),
                dbc.CardHeader("Sobre el módulo y sus reportes", style={'textAlign': 'center', "font-weight":"bold"}),
                dbc.CardBody(
                    html.P("""El módulo esta diseñado para vizualizar diferencias en panorama politico y demografico."""),
                ),
            ]),
        ]),
        dbc.Col([
            dbc.Card([
                dbc.CardImg(),
                dbc.CardHeader("Sobre este ánalisis", style={'textAlign': 'center', "font-weight":"bold"}),
                dbc.CardBody(
                        html.P("""Se analizará la demografía de los votantes, desglosando la información según características
                               como intereses ubicación; al comprender mejor el perfil de los votantes y los tipos de intereses, se podrá identificar 
                               posibles patrones y tendencias, esto ayudará a enfocar los esfuerzos en áreas específicas y tomar medidas adecuadas. 
                               Además se verá la distribución geográfica de los votantes en diferentes zonas. 
                               Esto permitirá identificar áreas con una mayor concentración de votantes, ver su priorización y en consecuencia , enfocar los recursos y esfuerzos en esas áreas para abordar los
                               problemas de manera más efectiva."""),
                ),
            ]),
        ]),   
    ]),
    dbc.Row(style={'margin-top': '20px'}),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardImg(src="assets/images/dashboards.jpg", style={'width': '30%', 'height': 'auto', 'margin': '0 auto','padding': '20px'}, className='text-center'),
                dbc.CardBody(
                    html.P("Las bases de datos empleadas para este análisis son propiedad privada", style={'textAlign': 'center'}),
                ),
            ]),
        ]),
    ], style={'margin-top': '20px'}),
])

#Side menu cards
demographics_card = sidecard("Demografía", "Perfil de los votantes", "/demographics")
infections_card = sidecard("Mapas por estados", "Distribución de votos por Estados", "/mapas_est")
alerts_card = sidecard("Mapas por Municipios", "Distribución de votos por Municipios", "/mapas_mun")
earlyalerts_card = sidecard("Mapas por parroquias", "Distribución de votos por Parroquias", "/mapas_par")

#Define layout
layout = html.Div(
    [
    dbc.Row(
        [
        dbc.Col(
            [
            dbc.Row(demographics_card),
            dbc.Row(infections_card),
            dbc.Row(alerts_card),
            dbc.Row(earlyalerts_card),
            ], width=2,
            ),
        dbc.Col(content_home),
        ],
        align="start",
        justify="between"
        ),          
    ]
)