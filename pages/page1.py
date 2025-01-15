from dash import html, dcc, register_page, Input, Output, callback
import os

register_page(__name__, path="/page1")

layout = html.Div([ 
    html.H2("DashBoard 1: Matthieu", style={'text-align': 'center'})
    ])  

# @callback(
# )
# def function():
#     return


