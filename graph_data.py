import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
from variables import *


############################################ Economy ############################################

# GDP
trace = [go.Choropleth(
               colorscale = 'blues',
               locationmode = 'country names',
               locations = gdp_data['country'],
               text = gdp_data['country'],
               z = gdp_data['gdp']
               )]
layout = go.Layout(title = 'GDP in European Countries',
                  geo = go.layout.Geo(
                       scope = 'europe',
                       showcountries = True))

fig_gdp = go.Figure(data = trace, layout = layout)
fig_gdp.update_layout(margin={"r":0,"t":30,"l":0,"b":0})

# low savings

fig_low_savings = px.bar(low_savings_data, x='country', y='prct_low_savings', title="Percent Low savings", labels={
                     "prct_low_savings": "Low Savings (%)"})


# median income VS population

fig_median_income_population = px.scatter(euro_stats_data, y="median_income", x="total_pop",size="median_income" ,color="country", hover_name="country", labels={
                     "total_pop": "Total Population (M)", 'median_income': 'Median Income (k)'})

########################################################################################



#fig_treemap = px.treemap(, path=['Country', 'Employment rate as pct', 'Long-term unemployment rate as pct'], values='Employment rate as pct', color='Employment rate as pct', hover_data=['Country', 'Employment rate as pct', 'Long-term unemployment rate as pct'])