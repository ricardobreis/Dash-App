from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc



# HOME CONTENT

layout = html.Div(children=[

    # Content
    html.Div(className="container container-content", 
        children=[

                # Jumbotron
                html.Div(
                    dbc.Container(
                        [
                            html.H1("Jumbotron", className="display-3"),
                            html.P(
                                "Use Containers to create a jumbotron to call attention to "
                                "featured content or information.",
                                className="lead",
                            ),
                            html.Hr(className="my-2"),
                            html.P(
                                "Use utility classes for typography and spacing to suit the "
                                "larger container."
                            ),
                            html.P(
                                dbc.Button("Sobre", color="primary"), className="lead"
                            ),
                        ],
                        fluid=True,
                        className="py-3",
                    ),
                    className="p-3 bg-light rounded-3 jumbotron",
                ),

                # Dashboard
                dbc.Row(
                    [
                        dbc.Col(dbc.Card(
                            [
                                dbc.CardHeader("Card header"),
                                dbc.CardBody(
                                    [
                                        html.H5("Card title", className="card-title"),
                                        html.P(
                                            "This is some card content that we'll reuse",
                                            className="card-text",
                                        ),
                                    ]
                                ),
                            ]
                            )),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardHeader("Card header"),
                                    dbc.CardBody(
                                        [
                                            html.H5("Card title", className="card-title"),
                                            html.P(
                                                "This is some card content that we'll reuse",
                                                className="card-text",
                                            ),
                                        ]
                                    ),
                                ]
                                )
                        ),
                        dbc.Col(dbc.Card(
                            [
                                dbc.CardHeader("Card header"),
                                dbc.CardBody(
                                    [
                                        html.H5("Card title", className="card-title"),
                                        html.P(
                                            "This is some card content that we'll reuse",
                                            className="card-text",
                                        ),
                                    ]
                                ),
                            ]
                            )),
                    ],
                    className="mb-4",
                ),
                
                

            ]
    ),

])