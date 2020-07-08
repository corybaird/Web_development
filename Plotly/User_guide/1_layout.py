# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
''''
Two parts to the app:
1. The "layout" describes what the application looks like. 
2. The remaining describes the interactivity of the application.
'''

#Tutorial from:
#https://dash.plotly.com/layout

#########################################Intialization, style, graph data#########################################

#CSS style sheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# This initializes the app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#Adds color to the background of the app
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# Assume you have a "wide-form" data frame with no index
df = pd.DataFrame({"x": [1, 2, 3], "SF": [4, 1, 2], "Montreal": [2, 4, 5]})

fig = px.bar(df, x="x", y=["SF", "Montreal"], barmode="group")

#Adds background colors to the chart
fig.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'])

#Markdown text to be added in the app
markdown_text = '''
### Dash and Markdown
# Header one
## Header two

[Plotly Link](https://dash.plotly.com/layout)
'''

#########################################Layout#########################################
'''
- The layout is composed of a tree of "components" like html.Div and dcc.Graph
- The dash_html_components library has a component for every HTML tag. 
    - The html.H1(children='Hello Dash') component generates a <h1>Hello Dash</h1> HTML element in your application.
- The children property is special and you can ommit it: html.H1(children='Hello Dash')==html.H1('Hello Dash')
'''

app.layout = html.Div(children=[
   
    #Title
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    #Subtitle 
    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    
   
    #Graph
    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    
    #Markdown text
    html.Div([
    dcc.Markdown(children=markdown_text)]),
])

if __name__ == '__main__':
    app.run_server(debug=True)