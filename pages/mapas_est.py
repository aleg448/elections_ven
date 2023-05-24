#Libraries
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

#Own functions
from components.cards.sidecard import sidecard

#from app import app

#Add home to page registry
register_page(__name__, path="/mapas_est", name="Inicio", title="Mapas politicos por estado", order=1)

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
        dbc.Col([html.H1("Brecha entre partido Chavista y oposicion"),
        html.Iframe(id="map", srcDoc=open(r"C:\Users\nadya\Downloads\venapp\ven-app-web\data\mapas\Mapa_estado_2020.html").read(), width="100%", height="600")       
]),
        ],
        align="start",
        justify="between"
        ),
            ] 
)