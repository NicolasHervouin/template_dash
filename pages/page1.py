from dash import html, dcc, register_page, Input, Output, callback
import pandas as pd
import plotly.express as px

# Charger les données (remplacez 'votre_fichier.csv' par le chemin vers votre fichier)
try:
    df = pd.read_csv('votre_fichier.csv')
except FileNotFoundError:
    print("Erreur : Fichier 'votre_fichier.csv' introuvable.")
    df = pd.DataFrame()  # Créer un DataFrame vide en cas d'erreur

register_page(__name__, path="/page1")

layout = html.Div([
    html.H2("DashBoard 1: Matthieu", style={'text-align': 'center'}),

    # Dropdown pour sélectionner la colonne à utiliser pour le graphique
    dcc.Dropdown(
        id='colonne-selection',
        options=[{'label': col, 'value': col} for col in df.columns],
        value=df.columns[0] if not df.empty else None,  # Sélectionner la première colonne par défaut si le DataFrame n'est pas vide
        placeholder="Sélectionnez une colonne"
    ),

    # Graphique Pie Chart
    dcc.Graph(id='pie-chart'),

    # Affichage d'informations supplémentaires
    html.Div(id='info-supplementaire')
])

@callback(
    Output('pie-chart', 'figure'),
    Input('colonne-selection', 'value')
)
def update_pie_chart(colonne_selection):
    """
    Met à jour le graphique Pie Chart en fonction de la colonne sélectionnée.

    Args:
        colonne_selection (str): Nom de la colonne sélectionnée dans le dropdown.

    Returns:
        plotly.graph_objects.Figure: Figure du Pie Chart.
    """
    if colonne_selection is None or df.empty:
        return px.pie(title="Données non disponibles")  # Retourner un graphique vide avec un message si aucune donnée n'est disponible

    fig = px.pie(df, names=colonne_selection, title=f"Répartition de {colonne_selection}")
    return fig

@callback(
    Output('info-supplementaire', 'children'),
    Input('colonne-selection', 'value')
)
def update_info_supplementaire(colonne_selection):
    """
    Affiche des informations supplémentaires sur la colonne sélectionnée.

    Args:
        colonne_selection (str): Nom de la colonne sélectionnée dans le dropdown.

    Returns:
        str: Texte à afficher dans la div 'info-supplementaire'.
    """
    if colonne_selection is None or df.empty:
        return "Aucune information supplémentaire disponible."

    # Calculer et afficher des statistiques (exemple)
    moyenne = df[colonne_selection].mean()
    return f"Moyenne de {colonne_selection}: {moyenne:.2f}"

# Callback supplémentaire (exemple : afficher le nombre de valeurs uniques)
@callback(
    Output('pie-chart', 'clickData'),  # Output factice pour déclencher le callback
    Input('colonne-selection', 'value')
)
def afficher_nombre_valeurs_uniques(colonne_selection):
    """
    Affiche le nombre de valeurs uniques dans la colonne sélectionnée dans la console.

    Args:
        colonne_selection (str): Nom de la colonne sélectionnée dans le dropdown.
    """
    if colonne_selection is not None and not df.empty:
        nombre_unique = df[colonne_selection].nunique()
        print(f"Nombre de valeurs uniques dans {colonne_selection}: {nombre_unique}")
    return None

