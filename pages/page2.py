#%% Chargement des librairies
from dash import Dash, html, dcc, Input, Output, callback, register_page
import pandas as pd
import plotly.express as px
import os

df = pd.read_csv('data/chickweight.csv', sep=',')
print(df.head())

#%% Création de l'application
register_page(__name__, path="/page2")

# Layout de la page
layout = html.Div(
    [
        html.H2("DashBoard 2: Arthur", style={"text-align": "center"}),


        # Dropdown pour sélectionner le poulet
        dcc.Dropdown(
            id="chick-dropdown",
            options=[
                {"label": f"Chick {chick}", "value": chick}
                for chick in df["Chick"].unique()
            ],
            value=df["Chick"].iloc[0],
            clearable=False,
            style={"width": "50%", "margin-bottom": "20px"},
        ),

        # Sélection de la période étudiée (plage de temps)
        html.Div(
            dcc.RangeSlider(
                id="time-slider",
                min=int(df["Time"].min()),  # Convertir en entier natif
                max=int(df["Time"].max()),  # Convertir en entier natif
                step=1,
                marks={int(t): str(t) for t in df["Time"].unique()},  # Assurez-vous que les clés sont des entiers natifs
                value=[int(df["Time"].min()), int(df["Time"].max())],  # Valeurs initiales
                tooltip={"placement": "bottom", "always_visible": True},
            ),
            style={"margin-bottom": "20px"},  # Styles appliqués au conteneur
        ),

        # Graphique
        dcc.Graph(
            id="weight-graph",
            style={
                "width": "80%",
                "height": "500px",
                "margin": "auto",
            },
        ),

        # Composant de message ou d'alerte
        html.Div(
            id="alert-message",
            style={"text-align": "center", "margin-top": "20px", "color": "red"},
        ),
    ]
)

# Callback 1 : Mettre à jour le graphique en fonction du Dropdown et du RangeSlider
@callback(
    Output("weight-graph", "figure"),
    [Input("chick-dropdown", "value"),
     Input("time-slider", "value")]
)
def update_graph(selected_chick, time_range):
    # Filtrer les données en fonction de la période sélectionnée et du poulet choisi
    filtered_df = df[
        (df["Chick"] == selected_chick) &
        (df["Time"] >= time_range[0]) &
        (df["Time"] <= time_range[1])
    ]
    # Créer le graphique avec la plage temporelle
    fig = px.line(
        filtered_df,
        x="Time",
        y="weight",
        title=f"Évolution du poids pour Chick {selected_chick}",
    )
    fig.update_layout(
        xaxis=dict(title="Temps (jours)"),
        yaxis=dict(title="Poids (grammes)"),
        margin=dict(l=40, r=40, t=50, b=40),
        width=700,
        height=400,
    )
    return fig

# Callback 2 : Message d'alerte si la plage sélectionnée est trop courte
@callback(
    Output("alert-message", "children"),
    [Input("time-slider", "value")]
)
def display_alert(time_range):
    # Exemple : Afficher un message si la plage de temps sélectionnée est très courte
    if time_range[1] - time_range[0] < 2:
        return "Attention : La période sélectionnée est très courte et peut ne pas afficher suffisamment de données."
    return ""  # Aucun message si la plage est correcte