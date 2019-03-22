import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()
app.layout = html.Div([
    dcc.Input(id='country', type="text", value='Czech rep'),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Div(id='output-state')
])

@app.callback(Output('output-state', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('country', 'value')])

def update_output(n_clicks, input):
    return '''
        The Button has been pressed {} times,
        input is "{}".
    '''.format(n_clicks, input)

if __name__ == '__main__':
    app.run_server(debug=True)
