from dash import html, dcc ,Dash
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.express as px

ski_resorts=pd.read_csv('Data\European_Ski_Resorts.csv',index_col=False).drop('Unnamed: 0',axis=1)
#df=df2.query("STATE =='WASHINTON' & YEAR >1992")

app=Dash(__name__)
app.layout=html.Div([
           html.H3(id='title'),
           dcc.Slider(
                   id='slider',
                   min=0,
                   max=4000,
                   step=500,
                   value=500,
                   marks={i:f'{i} Thousands Meters' for i in range(0,4001,500)}
           ),
           dcc.Checklist(
               id='dropdown',
               options=['Has Snow Park','Has Night Ski'],
               value=['Has Snow Park','Has Night Ski'] 
               
           ),
           dcc.Graph(
               id='graph'
           )

])

@app.callback(
Output('title','children'),
Output('graph','figure'),
Input('slider','value'),
Input('dropdown','value')

)
def linechart(elevation,features):
    title=f"Ski Resorts with Elevation Over {elevation} Meter Max Elevation"
    ski_resorts_filtered=ski_resorts.query('HighestPoint > @elevation')
    if features==[]:
        df3=(ski_resorts_filtered.groupby('Country',as_index=False)
             .agg(ResortCount = ('Country','count'))
        )
    elif len(features)==2:
         df3=(
            ski_resorts_filtered.query("Snowparks =='Yes'and NightSki =='Yes'")
            .groupby('Country',as_index=False)
            .agg(ResortCount = ('Country','count'))
         )
    elif features== ['Has Snow Park']:
          df3=(
             ski_resorts_filtered.query("Snowparks =='Yes'")
             .groupby('Country',as_index=False)
             .agg(ResortCount = ('Country','count'))
         )
    else:
          df3=(
             ski_resorts_filtered.query("NightSki =='Yes'")
             .groupby('Country',as_index=False)
             .agg(ResortCount = ('Country','count'))
         )
    figure=px.choropleth(
        df3,
        locations='Country',
        color='ResortCount',
        locationmode='country names',
        scope='europe'
    ).update_geos(fitbounds='locations').update_layout(margin={'r':0,'t':0,'l':0,'b':0})

    return title, figure


if __name__ == '__main__':
        app.run_server(debug=True) 