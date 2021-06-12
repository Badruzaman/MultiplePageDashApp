
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Bootstrap/Side-Bar/iranian_students.csv')

page_2_layout = html.Div([
    html.H1('High School in Iran',
            style={'textAlign': 'center'}),
    dcc.Graph(id='bargraph',
              figure=px.bar(df, barmode='group', x='Years',
                            y=['Girls High School', 'Boys High School']))
])