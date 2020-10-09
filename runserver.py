import dash
import dash_core_components as dcc
import dash_html_components as html
from graph_data import *
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(children=[
    html.H1(children='Analysis of Life in Europe', style={'color': 'ghostwhite', 'fontSize': 50, 'font-family': 'cursive' ,'text-align':'center', 'backgroundColor': '#311e73'}),
    html.H3(children='Created by:', style={'color': '#9fb4cc', 'fontSize': 24, 'text-align':'center', 'backgroundColor': '#140057'}),
    html.H2(children='Kunal PATIL (Artificial Intelligence System) & Salil MARATH-PONMADOM (Data Science and Analytics)', style={'color': '#efedf5', 'fontSize': 20, 'text-align':'center', 'backgroundColor': '#6b54ba'}),
    html.H3(children='######################################', style={'color': '#180847', 'fontSize': 10, 'text-align':'center', 'backgroundColor': '#180847'}),
    html.H5(children='''
        The aim is to analyse the data which compares multiple factors for European countries. To visualise and compare some of the key factors – 
        like education, housing, environment, and so many for 38 countries.''', style={'text-align':'center', 'fontSize': 18}),
    html.H3(children='######################################', style={'color': '#180847', 'fontSize': 10, 'text-align':'center', 'backgroundColor': '#180847'}),

html.H4(
        children="Economy",
        style={'color': '#44874e', 'fontSize': 24, 'text-align':'center'}),
    dcc.Graph(
        id='gdp',
        figure=fig_gdp
    ),
    html.H5(
        children="Observation and Comments: By observing above distribution, we can see that Countries like UK, France, Italy and Spain have highest GDP that other european countries, Whereas Germany have Highest GDP among all.",
        style={'color': 'black', 'fontSize': 16}),
dcc.Graph(
        id='low_savings',
        figure=fig_low_savings
    ),
html.H5(
        children="Observation and Comments: Countries like Bulgaria, Cyprus, Greece, Croatia, Lithuania, Romania have Lower savings that other european countries, Whereas Latvia have Lowest savings, 60%",
        style={'color': 'black', 'fontSize': 16}),
dcc.Graph(
        id='median_income_and_population',
        figure=fig_median_income_population
    ),
html.H5(
        children="Observation and Comments: Comparing population with respect to median income, Luxembourg has Highest median income and less population. "
                 "Romania have lowest median income but population is about 20M, whereas Germany having highest population almost 80M still have quite good median income about 21k",
        style={'color': 'black', 'fontSize': 16}),
html.H6(children='######################################', style={'color': '#180847', 'fontSize': 7, 'text-align':'center', 'backgroundColor': '#180847'})
    ])
if __name__ == '__main__':
    app.run_server(debug=True)