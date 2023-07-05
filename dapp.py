#imports 
from dash import Dash, html, dash_table,dcc,callback,Output,Input
import  pandas as pd 
import plotly.express as px
#import dash_design_kit as ddk
df=pd.read_excel('stock.xlsx',index_col=False,nrows=500)
# Initialize the app - incorporate css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = html.Div([
    html.Div(className='row', children='Stock Analysis',
             style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),
    html.Hr(),
    html.Div(className='row', children=[
        dcc.RadioItems(options=['Volume', 'Low', 'High'],
                       value='Volume',
                       inline=True,
                       id='my-radio-buttons-final')
    ]),

    html.Div(className='row', children=[
        html.Div(className='six columns', children=[
            dash_table.DataTable(data=df.to_dict('records'), page_size=11, style_table={'overflowX': 'auto'})
        ]),
        html.Div(className='six columns', children=[
            dcc.Graph(figure={}, id='histo-chart-final')
        ])
    ])
])

# Add controls to build the interaction
@callback(
    Output(component_id='histo-chart-final', component_property='figure'),
    Input(component_id='my-radio-buttons-final', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='Date', y=col_chosen, histfunc='avg')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
