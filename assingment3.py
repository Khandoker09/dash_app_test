from dash import html, dcc ,Dash
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.express as px

df=pd.read_csv('Data\spanish_skiers.csv',index_col=False)
#df=df2.query("STATE =='WASHINTON' & YEAR >1992")

app=Dash(__name__)
app.layout=html.Div([
           html.H3('Percentage of Spanish who skied each year'),
        #    dcc.Dropdown(
        #        id='dropdown',
        #        options=df['Year'].unique()
        #    ),
           dcc.Graph(
               id='visual',
                   figure=px.line(
                            df,
                            x='Year',
                            y='Percent_Skiers',
                            labels={'Percent_Skiers':'Percentage of People who Skied on that Specific Year'},
                            title=f'Percentage of Spanish who skied each year')
           )

])



if __name__ == '__main__':
        app.run_server(debug=True) 