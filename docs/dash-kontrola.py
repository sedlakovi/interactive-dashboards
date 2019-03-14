import base64
import gzip
import io
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

    # data = pd.read_csv('data_instalace.csv')
    # data.y -= 2
    # data.x += 10
    # data = data.to_numpy()[:, 1:]

    # data = (data * 4.2).astype(np.uint8)

    # np.save('x', data)

    data = np.load(io.BytesIO(gzip.decompress(base64.b85decode(POINTS))))

    trace = go.Scatter(
        x=data[:, 0],
        y=data[:, 1],
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

# Následují zakódované body grafu
POINTS = b'ABzYG83l@500Vd~Zg6=3olNnE+i)Dc{W5OKag<W3$C0f%-D;&<DJ6uE3E4s^b=_r3$*sNKLbeb>2(?<bDxs88LMf$`Qc5W$gi=Z=<=CIGPnvJKy6aDieBbBu-sipd>-|THPCq&Mdh!js=59Zguy;Z1``v3S9K=4~l**+mK6_KT=4|~#>5c>WHh=Yn1N!{U+h{l#eGv{y!T<f9d3}DLKX7r0?I08mg(Hz@G!~D=6Y)e6{!`D{xz~rT5x69hsUy-O1t-X43V=#DW9PyNWXF*WC)@-<?iP{)q-f_#GssOatkXg>Y#NPBb_Y2wU)TX(EZa{IM11c+x*$qNB$=eRJVoaVG*jRimM^mDVmX~D3z@7SW^<yH<0Ki}lB}rvjG}6lA3uLL^rkBy+G;x#k&c0k{{pS{;odQ9)-k$0n7#f0a4;OH+Gwm*#uM;OrZX^4XLCr*<|f4Erq$3*OK+Oi0vfEv5?TPEqYu&&T85)B<mNUz+?{!T=JCQied==tyfcp@f)eoi7@8spJe5quW6@VHL)hg-z|TGw(+@Qeof{I+&9&vS89PGYd?C--gd~dgN|EIvPg6qKW(@62F2^!O*U0V{G#DBUYKJUSt!SzuOQIXLueBp$y(S8cx+LliS!(Kv+-j;yyQQg}c11Hf)k@c>ReN2dQLk0|Fgxv5Q@4rJ<Vp_&mntYQIEaphhioz)4edFbP5{mM4A3(5#=>gqtK|Yb>(vshoAnA3+szt++fCQF-$Kcs`z>?<LMPy63T^g;$ijlI>Ew_(+h3lQUP@R5000'

if __name__ == '__main__':
    main()
