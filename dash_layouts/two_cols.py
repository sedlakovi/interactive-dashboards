import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div(
    className="row",
    children=[
        dcc.Graph(
            className="six columns",
            id='left-graph',
            figure={
                'data': [{
                    'x': [1, 2, 3],
                    'y': [3, 1, 2],
                    'type': 'bar',
                }],
            }
        ),
        dcc.Graph(
            className="six columns",
            id='right-top-graph',
            figure={
                'data': [{
                    'x': [1, 2, 3],
                    'y': [3, 1, 2],
                    'type': 'bar',
                    'marker': {'color': 'green'},
                }],
            }
        ),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
