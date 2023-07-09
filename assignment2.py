from dash import html, dcc ,Dash
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.express as px

df=pd.read_csv('Data\states_all.csv',usecols=['STATE','YEAR','TOTAL_EXPENDITURE'])
#df=df2.query("STATE =='WASHINTON' & YEAR >1992")

app=Dash(__name__)
app.layout=html.Div([
           html.H3('Interactiv Chart with Line Graph'),
           dcc.Dropdown(
               id='dropdown',
               options=df['STATE'].unique(),
               value=['CALIFORNIA','OREGON'],
               multi=True
           ),
           dcc.Graph(
               id='visual'
           )

])

@app.callback(
Output('visual','figure'),
Input('dropdown','value')
)
def linechart(STATE):
    if not STATE:
        raise PreventUpdate
    figure=px.line(
        df.query(f"STATE in @STATE"),
        x='YEAR',
        y='TOTAL_EXPENDITURE',
        color='STATE',
        title=f'Expenditure of the over time')
                  
          
    return figure


if __name__ == '__main__':
        app.run_server(debug=True) 