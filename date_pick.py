from dash import html, dcc ,Dash
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.express as px

df=pd.read_csv('Data/NYC_Collisions.csv',index_col=False)
#df=df2.query("STATE =='WASHINTON' & YEAR >1992")

app=Dash(__name__)
app.layout=html.Div([
           html.H3('Date Picker'),
           dcc.DatePickerSingle(
                   id='date picker',
                   min_date_allowed=df['ACCIDENT_DATE'].min(),
                   max_date_allowed=df['ACCIDENT_DATE'].max(),
                   initial_visible_month=df['ACCIDENT_DATE'].max(),
                   date=df['ACCIDENT_DATE'].max(),
                   display_format='YYYY-MM-DD'
                  
           ),
           dcc.Graph(
               id='graph',
           )
])

@app.callback(
        Output('graph','figure'),
        Input('date picker','date')
)
def plot(date):
        # if not elevation:
        #         raise PreventUpdate
        figure=px.bar(
                df.loc[df['ACCIDENT_DATE'].eq(date)],
                x='COLLISION_ID',
                y='BOROUGH'
        )
        return figure

if __name__ == '__main__':
        app.run_server(debug=True) 