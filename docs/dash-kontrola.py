import sys

if sys.version_info[0] < 3:
        print("Je potřeba nainstalovat Python 3. :-(")
        sys.exit(1)

import numpy as np
import pandas as pd
from plotly.offline import iplot, init_notebook_mode
import plotly.graph_objs as go

import dash.dependencies
import dash_html_components as html
import dash_core_components as dcc
import os
import pandas as pd
import plotly.graph_objs as go

import notebook


def main():
    app = dash.Dash()
    my_css_url = 'https://codepen.io/chriddyp/pen/bWLwgP.css'
    app.css.append_css({
        "external_url": my_css_url
    })


    data = pd.read_csv('data_instalace.csv')

    trace = go.Scatter(
        x=data.x,
        y=data.y,
        mode='markers'
    )
    data = [trace]
    layout = dict(
            width=1000,
            height=1000,
            xaxis=dict(
              title='',
              zeroline=False,
              showgrid=False
            ),
            yaxis=dict(
              title='',
              zeroline=False,
              showgrid=False
            ),
            hovermode='closest'
    )
    fig = dict(data=data, layout=layout)


    app.layout = html.Div(children=[
            dcc.Markdown('''# Kontrola instalace
            Pokud body vytvářejí smysluplné slovo, instalace proběhla uspěšně! Gratulujeme!'''),
            dcc.Graph(
                            figure=fig
            )
    ], style={'textAlign': 'center'})

    app.run_server()

if __name__ == '__main__':
    main()
