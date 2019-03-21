import dash
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
		'Stát: {}<br>Počet litrů čístého lihu na osobu ročně: {}'.format(row.country, row.total_litres_of_pure_alcohol)
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
		title = 'Počet litrů čístého lihu na osobu ročně',
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
	title='Celková spotřeba alkoholu na osobu ročně',
	geo=dict(
		# Zaměříme graf na střed Evropy
		center=dict(
			lon=14,
			lat=50
		),
		showframe=False,
		showcoastlines=False,
		projection=dict(
			type='equirectangular',
			#
			scale=3
		)
	)
)

fig = dict(data = data, layout = layout)

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
    dcc.Graph(id='drinks-map',
			  figure = fig,
			  clickData={'points':[{'location': 'CZE'}]}
			  ),
])


if __name__ == '__main__':
	app.run_server(debug=True)
