#Import Libraries
from dash import html
import dash_bootstrap_components as dbc

def sidecard(label, description, href):
    card=html.Div([
            dbc.Card(
            [
            dbc.CardBody([
                html.H6(label, style={"font-weight":"bold"}, className="card-title"),
                html.P(description,className='card_text'),
                dbc.Button("Más información", color="dark", href=href, size="sm", class_name="mr-1", id="menu_button", n_clicks=0,),
                ],
                class_name='m-2',
                style={"color":"#838383"},
                )
            ],
            )
        ])
    return card