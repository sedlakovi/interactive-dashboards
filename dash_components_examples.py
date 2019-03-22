from datetime import datetime as dt
import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()
app.layout = html.Div([
    dcc.DatePickerSingle(
        id='date-picker',
        date=dt(2019, 3, 1)
    ),
    dcc.Dropdown(
    id='example-dropdown',
      options=[
      {'label': 'Číst knihy', 'value': 'read'},
      {'label': 'Poslouchat hudbu', 'value': 'music'},
    ],
    value=''
    ),
    html.Div([dcc.RadioItems(
        options=[
            {'label': 'Číst knihy', 'value': 'read'},
            {'label': 'Poslouchat hudbu', 'value': 'music'}
        ],
        value='music'
    )], style={'width': '20%', 'display': 'block'}),
    html.Button('Klikněte zde!', id='button'),
])

if __name__ == '__main__':
	app.run_server(debug=True)
