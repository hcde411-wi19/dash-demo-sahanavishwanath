# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# initialize Dash app and initialize the static folder
app = dash.Dash(__name__, static_folder='static')
df = pd.read_csv('static/Pokemon.csv')

# filter for the Legendary Pokemon
legendary = df[df['Legendary'] == True]

# separate legendary Pokemon by generation
gen1_leg = legendary[legendary['Generation'] == 1]
gen2_leg = legendary[legendary['Generation'] == 2]
gen3_leg = legendary[legendary['Generation'] == 3]
gen4_leg = legendary[legendary['Generation'] == 4]
gen5_leg = legendary[legendary['Generation'] == 5]
gen6_leg = legendary[legendary['Generation'] == 6]

# set layout of the page
app.layout = html.Div(children=[

    # set the page heading
    html.H1(children='Exercise 2: Pokemon Scatter Plot'),

    # set the description underneath the heading
    html.Div(children='''
        This page shows a scatter plot that displays the attack and defense power of legendary Pokemon, separated
        by each generation.
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='exercise2-graph',
        figure={
            # Adding each generation data to scatter plot
            # Attack on the x axis, and defense on the y axis
            # Including name to clearly indicate which color corresponds to which generation
            # Including text so Pokemon name is shown when mouse hovers over point
            # Markers have some opacity to show overlapping data points
            'data': [

                go.Scatter(
                    x=gen1_leg['Attack'],
                    y=gen1_leg['Defense'],
                    name='Generation 1',
                    mode='markers',
                    text=gen1_leg['Name'],
                    marker={
                        'size': 15,
                        'opacity': 0.6
                    }
                ),
                go.Scatter(
                    x=gen2_leg['Attack'],
                    y=gen2_leg['Defense'],
                    name='Generation 2',
                    mode='markers',
                    text=gen2_leg['Name'],
                    marker={
                        'size': 15,
                        'opacity': 0.6
                    }
                ),
                go.Scatter(
                    x=gen3_leg['Attack'],
                    y=gen3_leg['Defense'],
                    name='Generation 3',
                    mode='markers',
                    text=gen3_leg['Name'],
                    marker={
                        'size': 15,
                        'opacity': 0.6
                    }
                ),
                go.Scatter(
                    x=gen4_leg['Attack'],
                    y=gen4_leg['Defense'],
                    name='Generation 4',
                    mode='markers',
                    text=gen4_leg['Name'],
                    marker={
                        'size': 15,
                        'opacity': 0.6
                    }
                ),
                go.Scatter(
                    x=gen5_leg['Attack'],
                    y=gen5_leg['Defense'],
                    name='Generation 5',
                    mode='markers',
                    text=gen5_leg['Name'],
                    marker={
                        'size': 15,
                        'opacity': 0.6
                    }
                ),
                go.Scatter(
                    x=gen6_leg['Attack'],
                    y=gen6_leg['Defense'],
                    name='Generation 6',
                    mode='markers',
                    text=gen6_leg['Name'],
                    marker={
                        'size': 15,
                        'opacity': 0.6
                    }
                )
            ],
            'layout': {
                # setting main title and axis titles
                'title': 'Legendary Pokemon Attack vs. Defense',
                'xaxis': {'title': 'Attack'},
                'yaxis': {'title': 'Defense'},
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
