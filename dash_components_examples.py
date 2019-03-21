from datetime import datetime as dt
import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

app = dash.Dash()
app.layout = html.Div([
    dcc.DatePickerSingle(
        id='date-picker',
        date=dt(2019, 3, 1)
    ),
    dcc.Dropdown(
    id='example-dropdown',
      options=[
      {'label': 'Read books', 'value': 'read'},
      {'label': 'Listen to music', 'value': 'music'},
    ],
    value=''
    ),
    html.Div([dcc.RadioItems(
        options=[
            {'label': 'Read books', 'value': 'read'},
            {'label': 'Listen to music', 'value': 'music'}
        ],
        value='music'
    )], style={'width': '20%', 'display': 'block'}),
    html.Button('Click me!', id='button'),
])

if __name__ == '__main__':
	app.run_server(debug=True)
