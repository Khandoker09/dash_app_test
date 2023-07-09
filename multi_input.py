from dash import html, dcc ,Dash
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.express as px

df=pd.read_csv('Data\states_all.csv',index_col=False)
#df=df2.query("STATE =='WASHINTON' & YEAR >1992")

app=Dash(__name__)
app.layout=html.Div([
           html.H3(id='header'),
           dcc.Dropdown(
               options=list(df.select_dtypes(include='number').columns),

               id='x column',
               #value='expenditure_per_student'
           ),
            dcc.Dropdown(
               options=list(df.select_dtypes(include='number').columns),

               id='y column',
               value='AVG_MATH_8_SCORE'
           ),
           dcc.Graph(
               id='graph',
           )
])

@app.callback(
        Output('header','children'),        
        Output('graph','figure'),
        Input('x column','value'),
        Input('y column','value')

)
def plot(x,y):
        # if not elevation:
        #         raise PreventUpdate

        figure=px.scatter(
                df,
                x=x,
                y=y,
                trendline='ols'
        )
        header=f"{x.title().replace('_','')} vs {y.title().replace('_','')} "
        return header,figure

if __name__ == '__main__':
        app.run_server(debug=True) 