from dash import html, dcc ,Dash
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.express as px

df=pd.read_csv('Data\European_Ski_Resorts.csv',index_col=False).drop('Unnamed: 0',axis=1)
#df=df2.query("STATE =='WASHINTON' & YEAR >1992")

app=Dash(__name__)
app.layout=html.Div([
           html.H3('Percentage of Spanish who skied each year'),
           dcc.Slider(
                   id='Elevation Slider',
                   min=0,
                   max=4000,
                   step=500,
                   marks={i:f'{i} Thousands Meters' for i in range(0,4000,500)}
           ),
           dcc.Graph(
               id='graph',
           )
])

@app.callback(
        Output('graph','figure'),
        Input('Elevation Slider','value')

)
def plot(elevation):
        if not elevation:
                raise PreventUpdate
        df2=(df.query('HighestPoint > @elevation').groupby('Country', as_index=False)
             .agg(Ski_Resorts_by_Country=('Country','count')))
        figure=px.bar(
                df2,
                x='Country',
                y='Ski_Resorts_by_Country'
        )
        return figure

if __name__ == '__main__':
        app.run_server(debug=True) 