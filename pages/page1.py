from dash import html, dcc, register_page, Input, Output, callback
import pandas as pd
import plotly.express as px

# Charger les données
try:
    df = pd.read_csv('chickweight.csv')
except FileNotFoundError:
    print("Erreur : Fichier 'chickweight.csv' introuvable.")
    df = pd.DataFrame()

register_page(__name__, path="/page1")

layout = html.Div([
    html.H2("DashBoard 1: Matthieu", style={'text-align': 'center'}),

    # Premier graphique : Pie Chart pour la distribution des valeurs d'une colonne
    html.Div([
        html.H3("Distribution des valeurs d'une colonne"),
        dcc.Dropdown(
            id='colonne-pie-chart',
            options=[{'label': col, 'value': col} for col in df.columns],
            value=df.columns[0] if not df.empty else None,
            placeholder="Sélectionnez une colonne"
        ),
        dcc.Graph(id='pie-chart')
    ]),

    # Deuxième graphique : Scatter plot pour l'évolution du poids en fonction du temps pour un poulet
    html.Div([
        html.H3("Evolution du poids en fonction du temps pour un poulet"),
        dcc.Dropdown(
            id='poulet-scatter-plot',
            options=[{'label': chick, 'value': chick} for chick in df['Chick'].unique()],
            value=df['Chick'].unique()[0] if not df.empty else None,
            placeholder="Sélectionnez un poulet"
        ),
        dcc.Graph(id='scatter-plot')
    ]),

    # Affichage d'informations supplémentaires
    html.Div(id='info-supplementaire')
])

@callback(
    Output('pie-chart', 'figure'),
    Input('colonne-pie-chart', 'value')
)
def update_pie_chart(colonne_selection):
    if colonne_selection is None or df.empty:
        return px.pie(title="Données non disponibles")

    fig = px.pie(df, names=colonne_selection, title=f"Distribution de {colonne_selection}")
    return fig

@callback(
    Output('scatter-plot', 'figure'),
    Input('poulet-scatter-plot', 'value')
)
def update_scatter_plot(poulet_selection):
    if poulet_selection is None or df.empty:
        return px.scatter(title="Données non disponibles")

    df_poulet = df[df['Chick'] == poulet_selection]
    fig = px.scatter(df_poulet, x='Time', y='weight', color='Diet', 
                     title=f"Evolution du poids du poulet {poulet_selection} en fonction du temps et du régime")
    return fig

# Callback pour afficher des informations supplémentaires (exemple)
@callback(
    Output('info-supplementaire', 'children'),
    Input('pie-chart', 'clickData')
)
def update_info_supplementaire(clickData):
    if clickData is None or df.empty:
        return "Cliquez sur une part du Pie Chart pour plus d'informations."

    valeur = clickData['points'][0]['label']
    colonne = clickData['points'][0]['customdata'][0]  # Récupérer le nom de la colonne
    nombre_occurrences = df[colonne].value_counts()[valeur]
    return f"Nombre d'occurrences de {valeur} dans la colonne {colonne}: {nombre_occurrences}"