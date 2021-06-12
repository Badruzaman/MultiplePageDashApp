import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

data = {'Product': ['Fuchka', 'Nachos', 'Baklava', 'Mug Dal', 'Paratha', 'Borhani', 'Ice Lime', 'Chotpoti', 'Extra Egg', 'Lava Cake'],
        'Amount': [5000, 6500, 8500, 7500, 6000, 9000, 10000, 8200, 9300, 9800]
        # ,'Color' : ['782a8e','954f9f','0898c4','33aee4', '08a978', '52bf9c', 'f47535', 'fdb71b', 'b71f3f', 'ef3d55']
        }
pdf = pd.DataFrame(data)
page_1_layout = html.Div([
    html.H1('Product Wise Sale(Top 10)', style={'textAlign': 'center'}),
    dcc.Graph(id='bargraph', figure=px.bar(pdf, x='Product', y='Amount', color='Product'))
])