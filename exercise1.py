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
            'data': [
                go.Bar(
                x= weekday_in_order,
                y= total_usage,
                name='Total',
                ),

                go.Bar(
                x= weekday_in_order,
                y= ped_n,
                name='Ped N',
                ),

                go.Bar(
                x= weekday_in_order,
                y= ped_s,
                name='Ped S',
                ),

                go.Bar(
                x= weekday_in_order,
                y= bike_n,
                name='Bike N',
                ),
                
                go.Bar(
                x= weekday_in_order,
                y= bike_s,
                name='Bike S',
                )
            ],

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
