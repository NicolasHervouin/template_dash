from dash import html, register_page

register_page(__name__, "/")

layout = html.Div(
    [   
        html.Div(
            [
                
                html.H2("Introduction", style={"text-align": "center"}),
                html.P(
                    """
                    Bienvenue sur notre dashboard.
                    """,
                    style={"text-align": "justify"}
                ),
            ],
                style={
                    "padding": "20px",
                    "border": "1px solid #ccc",
                    "border-radius": "10px",
                    "box-shadow": "2px 2px 5px rgba(0,0,0,0.1)",
                    "margin-bottom": "20px",
                },
        ),   
            
        html.Div(
            [        
                html.H2("Page 1 : Matthieu", style={"text-align": "left"}),
                html.P(
                    """
                    POULEUUUUUUH
                    """,
                    style={"text-align": "justify"}
                ),
            ],
            style={
                "padding": "20px",
                "border": "1px solid #ccc",
                "border-radius": "10px",
                "box-shadow": "2px 2px 5px rgba(0,0,0,0.1)",
                "margin-bottom": "20px",
            },
        ),
        html.Div(
            [
                html.H2("Page 2 : Arthur", style={"text-align": "left"}),
                html.P(
                    """
                    POULEUUUUUUH
                    """,
                    style={"text-align": "justify"}
                ),
            ],
            style={
                "padding": "20px",
                "border": "1px solid #ccc",
                "border-radius": "10px",
                "box-shadow": "2px 2px 5px rgba(0,0,0,0.1)",
            },
        ),
    ]
)
