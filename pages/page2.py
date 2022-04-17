from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc



# PAGE 2 CONTENT

layout = html.Div([

        # Content
        html.Div(className="container", 
            children=[
                    dbc.Row(
                        [
                            dbc.Col(html.Div(
                                children=[
                                    html.Div(
                                        [
                                            html.H2("PAGE2", className="display-4"),
                                            html.Hr(),
                                            html.P(
                                                "A simple sidebar layout with navigation links", className="lead"
                                            )
                                        ],
                                        className="sidebar",
                                    )
                                ]
                            ), width=3),
                            dbc.Col("Conteúdo", width=9),
                        ]
                    ),
                ],
            style={
                "padding-top" : "50px"
            }
        ),
    
])

