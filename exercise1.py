# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

# static data
weekday_in_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
total_usage = [160613, 154225, 155175, 150819, 146014, 215725, 203483]
ped_n = [26884, 26444, 25876, 24368, 23403, 36894, 32792]
ped_s = [28686, 27520, 27224, 25846, 24900, 37808, 34792]
bike_n = [52401, 49449, 50209, 49692, 47971, 69437, 67752]
bike_s = [52642, 50812, 51866, 50913, 49740, 71586, 68147]

# initialize Dash environment

app = dash.Dash(__name__)


total_usage_data = go.Bar(
    x= weekday_in_order,
    y= total_usage,
    name='Total',
    marker=go.bar.Marker(
    color='rgb(0, 0, 255)'
)

ped_n_data = go.Bar(
    x= weekday_in_order,
    y= ped_n,
    name='Ped N',
    marker=go.bar.Marker(
    color='rgb(255, 128, 0)'
)

ped_s_data = go.Bar(
    x= weekday_in_order,
    y= ped_s,
    name='Ped S',
    marker=go.bar.Marker(
    color='rgb(0, 153, 0)'
)

bike_n_data = go.Bar(
    x= weekday_in_order,
    y= bike_n,
    name='Bike N',
    marker=go.bar.Marker(
    color='rgb(255, 0, 0)'
)

bike_s_data = go.Bar(
    x= weekday_in_order,
    y= bike_s,
    name='Bike S',
    marker=go.bar.Marker(
    color='rgb(127, 0, 255)'
)

# set up an layout
app.layout = html.Div(children=[
    # H1 title on the page
    html.H1(children='Hello Dash for HCDE 411'),

    # a div to put a short description
    html.Div(children='''
        This is a simple Dash application for HCDE 411
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='exercise1-graph',
        figure={
            # configure the data
            'data':
            #[total_usage_data, ped_n_data, ped_s_data, bike_n_data, bike_s_data],
            {'x': weekday_in_order, 'y': total_usage, 'type': 'bar', 'name': 'Total'},
            {'x': weekday_in_order, 'y': ped_n, 'type': 'bar', 'name': 'Ped N'},
            {'x': weekday_in_order, 'y': ped_s, 'type': 'bar', 'name': 'Ped S'},
            {'x': weekday_in_order, 'y': bike_n, 'type': 'bar', 'name': 'Bike N'},
            {'x': weekday_in_order, 'y': bike_s, 'type': 'bar', 'name': 'Bike S'},

            # configure the layout of the visualization --
            # set the title to be "Usage of the BGT North of NE 70th per week day"
            'layout': {
                'title': 'Usage of the BGT North of NE 70th per week day'
            }
        }
    )
])


if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)
