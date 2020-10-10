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

fig_median_income_population = px.scatter(euro_stats_data, y="median_income", x="total_pop",title="Median Income Vs Population",size="median_income" ,color="country", hover_name="country", labels={
                     "total_pop": "Total Population (M)", 'median_income': 'Median Income (k)'})

########################################################################################
############################################ Employment ############################################

# Job Satisfaction
fig_job_satisfaction = go.Figure()
fig_job_satisfaction.add_trace(go.Bar(x=job_satisfaction_data['country'], y=job_satisfaction_data['prct_job_satis_high'], marker_color='green', name='High Satisfaction'))
fig_job_satisfaction.add_trace(go.Bar(x=job_satisfaction_data['country'], y=job_satisfaction_data['prct_job_satis_med'], marker_color='lightsteelblue',
                name='Medium Satisfaction'
                ))
fig_job_satisfaction.add_trace(go.Bar(x=job_satisfaction_data['country'], y=job_satisfaction_data['prct_job_satis_low'], marker_color='red',
                name='Low Satisfaction'
                ))
fig_job_satisfaction.update_layout(
    title="Job Satisfaction")

# Unemployment
fig_unemployment = px.line(unemployment_data, x="country", y="unemp_rate", title='Percentage of Unemployment', )

########################################################################################

############################################ Legal ############################################

fig_crime_rate = go.Figure(data=[go.Pie(labels=crime_data['country'], values=crime_data['prct_rpt_crime'], hole=.3, title="Crime Report Rate")])


# political_trust_rating,police_trust_rating,legal_trust_rating

fig_legal_trust_subplot = go.Figure()
fig_legal_trust_subplot.add_trace(go.Scatter(x=euro_stats_data['country'], y=euro_stats_data['political_trust_rating'],
                    mode='lines', line=dict(color='orange'),
                    name='Political Trust Rating'))
fig_legal_trust_subplot.add_trace(go.Scatter(x=euro_stats_data['country'], y=euro_stats_data['police_trust_rating'],
                    mode='lines', line=dict(color='darkslateblue'),
                    name='Police Trust Rating'))
fig_legal_trust_subplot.add_trace(go.Scatter(x=euro_stats_data['country'], y=euro_stats_data['legal_trust_rating'],
                    mode='lines', line=dict(color='magenta'), name='Legal Trust Rating'))
fig_legal_trust_subplot.update_layout(
    title="Trust on Legal, Political and Police Systems")



############################################################################################

very_good = go.Bar(
             x = health_data['country'],
             y = health_data['prct_health_verygood'],
             name = 'Very Good Health',
             marker = dict(color = '#99b898'),
)
good = go.Bar(
             x = health_data['country'],
             y = health_data['prct_health_good'],
             name = 'Good Health',
             marker = dict(color = '#fecea8'),
)
fair = go.Bar(
             x = health_data['country'],
             y = health_data['prct_health_fair'],
             name = 'Fair Health',
             marker = dict(color = '#ff847c'),
)
bad = go.Bar(
             x = health_data['country'],
             y = health_data['prct_health_bad'],
             name = 'Bad Health',
             marker = dict(color = '#e84a5f'),
)
very_bad = go.Bar(
             x = health_data['country'],
             y = health_data['prct_health_verybad'],
             name = 'Very Bad Health',
             marker = dict(color = '#2a3b36'),
)
data = [very_good, good, fair, bad, very_bad]
layout = go.Layout(title = 'Health in Europe',
                  barmode = 'relative')
fig_health_data = go.Figure(data = data, layout = layout)


# pollution
fig_pollution = px.bar_polar(euro_stats_data, r="prct_rpt_pollution", theta="country", color="prct_rpt_pollution", title="Percent Reported Pollution in Europe")

# life expectancy

trace = [go.Choropleth(
               colorscale = 'greens',
               locationmode = 'country names',
               locations = life_expectation_data['country'],
               text = life_expectation_data['country'],
               z = life_expectation_data['life_expect']
               )]
layout = go.Layout(title = 'Life Expectancy in Europe',
                  geo = go.layout.Geo(
                       scope = 'europe',
                       showcountries = True))

fig_life_expectation = go.Figure(data = trace, layout = layout)
fig_life_expectation.update_layout(margin={"r":0,"t":30,"l":0,"b":0})













