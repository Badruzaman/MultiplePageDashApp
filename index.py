import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from app import app
from apps.app1 import page_1_layout
from apps.app2 import page_2_layout
# Since we're adding callbacks to elements that don't exist in the app.layout,
# Dash will raise an exception to warn us that we might be
# doing something wrong.
# In this case, we're adding the elements through a callback, so we can ignore
# the exception.
# app = dash.Dash(__name__, suppress_callback_exceptions=True)

# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "Number of students per education level", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink('Go to Page 1', href='/page-1', active="exact"),
                dbc.NavLink('Go to Page 2', href='/page-2', active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content',children=[], style=CONTENT_STYLE),
    sidebar
])

index_page = html.Div([
    sidebar
])

# @app.callback(dash.dependencies.Output('page-1-content', 'children'),
#               [dash.dependencies.Input('page-1-dropdown', 'value')])
#
# def page_1_dropdown(value):
#     return 'You have selected "{}"'.format(value)
#
#
# @app.callback(dash.dependencies.Output('page-2-content', 'children'),
#               [dash.dependencies.Input('page-2-radios', 'value')])
# def page_2_radios(value):
#     return 'You have selected "{}"'.format(value)


# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here


if __name__ == '__main__':
    app.run_server(debug=True)
