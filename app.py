import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import plotly.graph_objs as go

# Data již byla předzpracována v Jupyter Notebooku plotly.ipynb
drinks = pd.read_csv('drinks_country_codes2.csv')

# Vytvoříme seznam popisků
text = []
for i, row in drinks.iterrows():
	text.append(
		'Country: {}<br>Total litres of pure alcohol per person per year: {}'.format(row.country, row.total_litres_of_pure_alcohol)
	)
# Pro vykreslení použijeme typ choropleth
data = [dict(
	type = 'choropleth',
	# Pro zobrazení použijeme hotovou barevnou škálu Jet
	colorscale = 'Jet',
	autocolorscale = False,
	locations = drinks.country_code_3,
	z = drinks.total_litres_of_pure_alcohol.astype(float),
	text = text,
	marker = dict(
		line = dict(
			color = 'rgb(255,255,255)',
			width = 2
		)),
	# Popišeme legendu
	colorbar = dict(
		title = 'Total litres of pure alcohol per person per year',
		# Následující parametry nastavují poměr délky legendy k obrázku a její pozici
		# len = 0.3,
		# y = 0.45
	)
)]

# Pro vykreslení celého světu použijeme typ projekce Mercator
layout = dict(
	# autosize = False,
	# width = 1000,
	height = 300,
	margin=dict(l = 0, r = 0, t = 0, b = 0),
	geo=dict(
		center=dict(
			lon=14,
			lat=50
		),
		showframe=False,
		showcoastlines=False,
		projection=dict(
			type='equirectangular',
			scale=3
		)
	)
)

fig = dict(data = data, layout = layout)

app = dash.Dash(__name__)
server = app.server
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
app.layout = html.Div(children=[
    html.H1(
        children='Total alcohol consumption per person per year',
    ),
    dcc.Markdown(
		'''
Data are taken from [FiveThirtyEight](https://github.com/fivethirtyeight/data/tree/master/alcohol-consumption)
		'''
	),
    dcc.Graph(id='drinks-map',
			  figure = fig,
			  clickData={'points':[{'location': 'CZE'}]}
			  ),
	html.Div([dcc.Graph(id='drinks-bar')], style={
		'width': '50%', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'
	})
])


@app.callback(
	Output(component_id='drinks-bar', component_property='figure'),
	[Input(component_id='drinks-map', component_property='clickData')],
)
def update_country_graph(clickData):
	#country_code = clickData['points']['location']
	drinks_country = drinks[drinks.country_code_3 == clickData['points'][0]['location']].head(1)
	trace1 = go.Bar(x = [0], y = drinks_country.beer_servings.values, name = 'Beer', width=0.5, marker=dict(color='#ef6236'))
	trace2 = go.Bar(x = [1], y = drinks_country.wine_servings.values, name = 'Wine', width=0.5, marker=dict(color='#811a17'))
	trace3 = go.Bar(x = [2], y = drinks_country.spirit_servings.values, name = 'Spirit', width=0.5, marker=dict(color='#5fdff1'))
	data = [trace1, trace2, trace3]

	layout = go.Layout(
		title = 'Average serving sizes per person - {}'.format(drinks_country.iloc[0].country),
		width = 700,
		showlegend = False,
		xaxis = dict(
			tickvals = [0, 1, 2],
			ticktext = ['Beer', 'Wine', 'Spirit'],
			tickangle = 60
		),
		yaxis = dict(
			title = 'Average serving sizes per person per year'
		)
	)
	figure = dict(data = data, layout = layout)
	return figure

if __name__ == '__main__':
	app.run_server(debug=True)
