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
                                        style={
                                            "width": "300px",
                                            "padding": "2rem 1rem",
                                            "background-color": "#f8f9fa",
                                        },
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


@callback(Output('page-2-display-value', 'children'), Input('page-2-dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'