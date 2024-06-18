import dash
from dash import dcc,html
import plotly_express as px
import pandas as pd

df = pd.read_excel('data.xlsx')

n = 10
fig = px.pie(df.head(n), names='Country', values='Official figure', 
                 title=f'Top {n} countries in Africa as a percentage of total',
                 hole=0.3,  # This makes it a doughnut plot
                 color_discrete_sequence=px.colors.qualitative.Pastel)  # Change the color template

fig.update_layout(
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.2,
        xanchor="center",
        x=0.5
    )
)

fig2 = px.bar(df.head(55),x = 'Country',y ="Official figure",template =None,title = "barplot of country ppn" )

fig3 = px.histogram(df, x='Official figure', title='Distribution of Official Figures',
                   labels={'Official figure': 'Population (in millions)'}, 
                   color_discrete_sequence=['#636EFA'])


app = dash.Dash(__name__)

app.layout = html.Div([
    #html.H1("Data visualization with dash"),
    html.Div(
        [
            html.Div(dcc.Graph(figure  =  fig),style = {"width":"40%"}),
            html.Div(dcc.Graph(figure = fig3),style = {"width":"40%"}),
            ],style = {'display':'flex'}),
    
    html.Div(dcc.Graph(figure = fig2))
],style = {"display":"inline"})

if __name__ =='__main__':
    app.run_server(debug = True)