# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# initialize Dash app and initialize the static folder
app = dash.Dash(__name__, static_folder='static')
df = pd.read_csv('static/Pokemon.csv')

legendary = df[df['Legendary'] == True]
gen1_leg = legendary[legendary['Generation'] == 1]
gen2_leg = legendary[legendary['Generation'] == 2]
gen3_leg = legendary[legendary['Generation'] == 3]
gen4_leg = legendary[legendary['Generation'] == 4]
gen5_leg = legendary[legendary['Generation'] == 5]
gen6_leg = legendary[legendary['Generation'] == 6]

# set layout of the page
app.layout = html.Div(children=[

    # set the page heading
    html.H1(children='Scatter Plot'),

    # set the description underneath the heading
    html.Div(children='''
        A demo to show a scatter plot.
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='exercise2-graph',
        figure={
            # configure the data
            'data': [
                # This is how we define a scatter plot. Note that it also uses "go.Scatter",
                # but with the mode to be only "markers"
                go.Scatter(
                    x=gen1_leg['Attack'],
                    y=gen1_leg['Defense'],
                    mode='markers',
                    text=gen1_leg['Name'],  # This line sets the vehicle name as the points' labels.
                    marker={
                        'size': 15,
                        'opacity': 0.6  # By making the points a bit transparent, it can alleviate the occlusion issue
                    }
                ),
                go.Scatter(
                    x=gen2_leg['Attack'],
                    y=gen2_leg['Defense'],
                    mode='markers',
                    text=gen2_leg['Name'],  # This line sets the vehicle name as the points' labels.
                    marker={
                        'size': 15,
                        'opacity': 0.6  # By making the points a bit transparent, it can alleviate the occlusion issue
                    }
                ),
                go.Scatter(
                    x=gen3_leg['Attack'],
                    y=gen3_leg['Defense'],
                    mode='markers',
                    text=gen3_leg['Name'],  # This line sets the vehicle name as the points' labels.
                    marker={
                        'size': 15,
                        'opacity': 0.6  # By making the points a bit transparent, it can alleviate the occlusion issue
                    }
                ),
                go.Scatter(
                    x=gen4_leg['Attack'],
                    y=gen4_leg['Defense'],
                    mode='markers',
                    text=gen4_leg['Name'],  # This line sets the vehicle name as the points' labels.
                    marker={
                        'size': 15,
                        'opacity': 0.6  # By making the points a bit transparent, it can alleviate the occlusion issue
                    }
                ),
                go.Scatter(
                    x=gen5_leg['Attack'],
                    y=gen5_leg['Defense'],
                    mode='markers',
                    text=gen5_leg['Name'],  # This line sets the vehicle name as the points' labels.
                    marker={
                        'size': 15,
                        'opacity': 0.6  # By making the points a bit transparent, it can alleviate the occlusion issue
                    }
                ),
                go.Scatter(
                    x=gen6_leg['Attack'],
                    y=gen6_leg['Defense'],
                    mode='markers',
                    text=gen6_leg['Name'],  # This line sets the vehicle name as the points' labels.
                    marker={
                        'size': 15,
                        'opacity': 0.6  # By making the points a bit transparent, it can alleviate the occlusion issue
                    }
                )
            ],
            'layout': {
                'title': 'Legendary Pokemon Attack vs. Defense',
                # It is always a good practice to have axis labels.
                # This is especially important in this case as the numbers are not trivial
                'xaxis': {'title': 'Attack'},
                'yaxis': {'title': 'Defense'},
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
