from dash import Dash, html, dcc
from dash.dependencies import Input,Output

app=Dash(__name__)

app.layout=html.Div([
           'pick a color',

           dcc.Dropdown(
               options=['Red','Blue','Green','Black','White'],

               id='color-input',
               value='Red'
           ),
           html.Div(id='color-output')
])

@app.callback(
            Output('color-output','children'),
            Input('color-input','value'))


def funtion_name(color):
        # if not color:
        #       raise PreventUpdate
        return f'Output:{color}'

if __name__ =='__main__':
    app.run_server(debug=True,port=8080)