# -*- coding: utf-8 -*-
"""
Created on Thu May 11 09:21:25 2023

@author: Gabo0
"""

#Import Libraries
import dash
from dash import html
import dash_labs as dl
import dash_bootstrap_components as dbc

#Own functions
from components.cards.infocard import infocard

#Create App
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO], plugins=[dl.plugins.pages],
                meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}])

app.config.suppress_callback_exceptions=True

app.title = "Fusion center"

# Create Navigation bar
navbar = dbc.NavbarSimple(
    children = [
        dbc.Row(
            [
                dbc.Col(dbc.DropdownMenu
                    (
                        children=[
                            dbc.DropdownMenuItem(page["name"], href=page["path"])
                            for page in dash.page_registry.values()
                            if page["module"] != "pages.not_found_404"],
                        nav=True,
                        in_navbar=True,
                        label="Menu",
                        color="white"
                    )
                ),
            ]
        )
    ],
    brand="Dashboard para el monitoreo de votantes",
    brand_href="#",
    color="black",
    dark=True
)

#Branding row
info_card = infocard("Fusion center\n Data Science", "assets/images/fc.png")

#Main layout
app.layout = dbc.Container(
    [
        dbc.Row(navbar),
        dbc.Row(dl.plugins.page_container),
        dbc.Row(info_card, justify="between")
    ],
    class_name="dbc",
    fluid=True,
)

# This call will be used with Gunicorn server
server = app.server

# Testing server
if __name__ == "__main__":
    app.run_server(debug=True, host="127.0.0.1", port=8050)