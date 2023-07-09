from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

app=Dash(__name__)

app.layout=html.Div([
        html.H2('_______________Result Preview_______________'),
          'Select a state Analyze:',
          dcc.Dropdown(
           options=['Oregon','Georgia','New York','Michigan','Washington DC','Los Angels','California'],
           #value='California',              
           id='state-input' 
          ),
        html.Div(id='state-output')
])
@app.callback(
  Output('state-output','children'),
  Input('state-input','value')
)

def state(state_variable):
    if not state_variable:
        raise PreventUpdate

    return f'State Selected:{state_variable}'

if __name__=='__main__':
    app.run_server(debug=True,port=8000)