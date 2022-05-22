from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import flask

# Import all application pages
from pages import home, page1, page2

server = flask.Flask(__name__)
# Add boostrap theme in 'external_stylesheets'
app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO], suppress_callback_exceptions=True)


# PAGE LAYOUT

app.layout = html.Div([

    # URL
    dcc.Location(id='url', refresh=False),

    # Header
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/", active="exact")),
            dbc.NavItem(dbc.NavLink("Page 1", href="/page1", active="exact")),
            dbc.NavItem(dbc.NavLink("Page 2", href="/page2", active="exact"))
        ],
        brand="Dash App",
        brand_href="#",
        color="primary",
        dark=True,
    ),

    # Content
    html.Div(id='page-content')
])



# ROUTE'S CONTROL

@callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return home.layout
    elif pathname == '/page1':
        return page1.layout
    elif pathname == '/page2':
        return page2.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True) 