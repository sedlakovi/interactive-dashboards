import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import plotly.graph_objs as go

# Data již byla předzpracována v Jupyter Notebooku plotly.ipynb
drinks = pd.read_csv('drinks_country_codes2.csv')


app = dash.Dash()
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
app.layout = html.Div(children=[
    html.H1(
        children='Celková spotřeba alkoholu na osobu ročně',
    ),
    dcc.Markdown(
		'''
Data jsou z [FiveThirtyEight](https://github.com/fivethirtyeight/data/tree/master/alcohol-consumption)
		'''
	),
    dcc.Dropdown(id='dropdown-country',
				 options = [{'label': country, 'value': country} for country in sorted(
					 drinks.country.unique()
				 )],
				 value = 'Czech Republic'
			  ),
	html.Div([dcc.Graph(id='drinks-bar')], style={
		'width': '50%', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'
	})
])


@app.callback(
	Output(component_id='drinks-bar', component_property='figure'),
	[Input(component_id='dropdown-country', component_property='value')],
)
def update_country_graph(country):
	drinks_country = drinks[drinks.country == country].head(1)
	trace1 = go.Bar(x = [0], y = drinks_country.beer_servings.values, name = 'Pivo', width=0.5, marker=dict(color='#ef6236'))
	trace2 = go.Bar(x = [1], y = drinks_country.wine_servings.values, name = 'Víno', width=0.5, marker=dict(color='#811a17'))
	trace3 = go.Bar(x = [2], y = drinks_country.spirit_servings.values, name = 'Tvrdý alkohol', width=0.5, marker=dict(color='#5fdff1'))
	data = [trace1, trace2, trace3]

	layout = go.Layout(
		title = 'Počet jednotek na osobu - {}'.format(country),
		width = 700,
		showlegend = False,
		xaxis = dict(
			tickvals = [0, 1, 2],
			ticktext = ['Pivo', 'Víno', 'Tvrdý alkohol'],
			tickangle = 60
		),
		yaxis = dict(
			title = 'Počet jenotek'
		)
	)
	figure = dict(data = data, layout = layout)
	return figure

if __name__ == '__main__':
	app.run_server(debug=True)
