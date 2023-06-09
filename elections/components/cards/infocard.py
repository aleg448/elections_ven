# -*- coding: utf-8 -*-
"""
Created on Thu May 11 10:13:56 2023

@author: Gabo0
"""

#Import Libraries
from string import capwords
from dash import html
import dash_bootstrap_components as dbc

def infocard(text,image):
    card=dbc.Card([
        dbc.Row([
            dbc.Col([
                dbc.CardBody([
                    html.P(text, className="card_text")
                ],style={"color":"#838383", 'textAlign': 'left', 'padding':'20 px'}
                )
            ]),
            dbc.Col(dbc.CardImg(src=image, class_name="w-75 mb-3"), width=1)
        ])
    ])
    return card