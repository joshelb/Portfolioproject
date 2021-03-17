import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
from priceimpact.scrapingmodule import DataStream as ds
from priceimpact.scrapingmodule import orderimpact
import  numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

global orderlist
orderlist = np.zeros(800)

app = DjangoDash("SimpleExample", external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Graph(
        id = 'candlestick-graph',

    ),
    dcc.Interval(
        id='interval-component',
        interval=10000,
        n_intervals=0
    )
])

@app.callback(Output('candlestick-graph','figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    data = {
        'time' : [],
        'open' : [],
        'high' : [],
        'low' : [],
        'close' : [],
        'orderdelta' : [],

    }

    df = ds.get_price_data("1m","BTCUSDT")
    orderdf = ds.get_order_data("BTCUSDT")
    for i in range(800):
        time = df["open_time"].iloc[i]
        open = df["open"].iloc[i]
        close = df["close"].iloc[i]
        high = df["high"].iloc[i]
        low = df["low"].iloc[i]

        data['time'].append(time)
        data['open'].append(open)
        data['close'].append(close)
        data['high'].append(high)
        data['low'].append(low)

    global orderlist
    orderlist = orderimpact.rollingorderimpact(orderlist,orderimpact.calculateDelta(orderdf))
    data['orderdelta'] = orderlist



    layout = go.Layout(
        title="My Dash Graph",
        height=700
    )
    fig = plotly.tools.make_subplots(rows=2,cols=1,vertical_spacing = 0.2)
    #fig.layout = layout

    fig.append_trace(
        go.Candlestick(x=data['time'],
                       open=data['open'],
                       high=data['high'],
                       low=data['low'],
                       close=data['close']),
        1,1
    )
    base = datetime.datetime.today()
    dates = base - np.arange(180) * datetime.timedelta(days=1)
    print(data['orderdelta'])


    fig.append_trace(
        go.Heatmap(

            z = [data['orderdelta']],
            x=data['time'],
            colorscale='Viridis',
            zmin=-100,
            zmax=100
        ),

        2,1
    )




    fig.update_layout(xaxis_rangeslider_visible=False)
    return fig