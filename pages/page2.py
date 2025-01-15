from dash import html, dcc, register_page, Input, Output, callback
import os

register_page(__name__, path="/page2")

layout = html.Div([ 
    html.H2("DashBoard 2: Arthur", style={'text-align': 'center'})
    ])  

@callback(
)
def function():
    return


