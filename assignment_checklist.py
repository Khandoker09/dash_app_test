from dash import html, dcc ,Dash
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.express as px

df2=pd.read_csv('Data\European_Ski_Resorts.csv',index_col=False).drop('Unnamed: 0',axis=1)
#df=df2.query("STATE =='WASHINTON' & YEAR >1992")

app=Dash(__name__)
app.layout=html.Div([
           html.H3('Interactiv Chart with Line Graph'),
           dcc.Checklist(
               id='dropdown',
               options=['Has Snow Park','Has Night Ski'],
               value=['Has Snow Park','Has Night Ski'] 
               
           ),
           dcc.Graph(
               id='visual'
           )

])

@app.callback(
Output('visual','figure'),
Input('dropdown','value')
)
def linechart(features):
    if features==[]:
        df=(df2.groupby('Country',as_index=False).agg({'TotalLifts':'sum'})
        )
    elif len(features)==2:
         df=(
             df2.query("Snowparks =='Yes'and NightSki =='Yes'").groupby('Country',as_index=False).agg({'TotalLifts':'sum'})
         )
    elif features== ['Has Snow Park']:
          df=(
             df2.query("Snowparks =='Yes'").groupby('Country',as_index=False).agg({'TotalLifts':'sum'})
         )
    else:
          df=(
             df2.query("NightSki =='Yes'").groupby('Country',as_index=False).agg({'TotalLifts':'sum'})
         )
    figure=px.choropleth(
        df,
        locations='Country',
        color='TotalLifts',
        locationmode='country names',
        scope='europe'
    ).update_geos(fitbounds='locations').update_layout(margin={'r':0,'t':0,'l':0,'b':0})
    title=f'{features}'
    return figure


if __name__ == '__main__':
        app.run_server(debug=True) 