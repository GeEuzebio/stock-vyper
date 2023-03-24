from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from dash_bootstrap_components.themes import CYBORG


app = Dash(__name__, 
           external_stylesheets = [CYBORG, '/assets/style.css'],
           suppress_callback_exceptions=True)

app.layout = dbc.Row(
        dbc.Col([
            dbc.Row([
                html.Img(src='/assets/img/vyper_logo_1.png', 
                         style={'width':'500px'},
                         id='vyper-img'),
                dbc.Button('Entre', 
                           id='entre',
                           n_clicks=0, 
                           style={'width':'80px', 
                                  'height':'40px',
                                  'background-color':'#ed1f34'},
                           className = 'button'),
                html.Div(children=[], id='login-popup')
            ], 
            style={'width':'100vw',
                      'height':'100vh',
                      'margin':'auto',
                      'display':'flex',
                      'flex-direction':'column',
                      'align-items':'center',
                      'justify-content':'space-evenly'}, 
            id='body')
    ])
    )

@app.callback(
    [Output('login-popup', 'children'),
     Output('body', 'style')],
    Input('entre', 'n_clicks')
)

def login_popup(n_clicks):
    if n_clicks>0:
        return html.Div([
                    html.Img(
                             id='close',
                             src='/assets/img/close.png', 
                             width='10px', 
                             style={'position':'relative', 
                                    'left':'280px',
                                    'top':'25px'},
                             n_clicks=0,
                             className='close'),
                    html.Div([
                        html.H3('Acessar Portal', style={'color':'#ed1f34'}),
                        html.Div([
                            html.P('Usuário', style={'color':'#ed1f34'}),
                            dcc.Input(id='username',
                                    type='text',
                                    placeholder='usuário',
                                    autoComplete='username')], style={
                                    'display':'flex',
                                    'flex-direction':'column',
                                    'align-items':'flex-start'
                                    }),
                        html.Div([
                            html.P('Senha', style={'color':'#ed1f34'}),
                            dcc.Input(id='password',
                                    type='password',
                                    placeholder='senha',
                                    autoComplete='username')], style={
                                    'display':'flex',
                                    'flex-direction':'column',
                                    'align-items':'flex-start'
                                    }),
                        html.Div([
                            dcc.Link('Esqueci a senha', href='#', style={'color':'#ed1f34'}),
                            html.Button('Login',
                                       id='login-button', 
                                       style={'width':'100px', 
                                              'height':'40px',
                                              'background-color':'#ed1f34'},
                                       className = 'button')
                         ], 
                         style={'width':'100%',
                                'display':'flex', 
                                'align-items':'center', 
                                'justify-content':'space-around'})],
                            style={'width':'300px', 
                                    'height':'400px', 
                                    'border':'solid 1px transparent', 
                                    'border-radius':'5px', 
                                    'box-shadow':'0 0 25px #ed1f34',
                                    'display':'flex',
                                    'flex-direction':'column',
                                    'align-items':'center',
                                    'justify-content':'space-around'},
                            id='portal-div')
                ], style={'position':'absolute',
                          'left':'40.2%',
                          'top':'100px',
                          'background-color':'#000'}), {'width':'100vw',
                      'height':'100vh',
                      'margin':'auto',
                      'display':'flex',
                      'flex-direction':'column',
                      'align-items':'center',
                      'justify-content':'space-evenly',
                      'backdrop-filter':'blur(5px)'}
    else:
        return (html.Div(), {'width': '100vw', 
                             'height': '100vh', 
                             'margin': 'auto', 
                             'display': 'flex', 
                             'flex-direction': 'column', 
                             'align-items': 'center', 
                             'justify-content': 
                             'space-evenly', 
                             'backdrop-filter': 'blur(5px)'})
    
@app.callback(
    [Output('portal-div', 'style'),
     Output('close', 'style')],
    Input('close', 'n_clicks')
)
def close_div(n_clicks):
    if n_clicks > 0:
        return [{'display': 'none'}, {'display': 'none'}]
    else:
        return [{'width':'300px', 
                 'height':'400px', 
                 'border':'solid 1px transparent', 
                 'border-radius':'5px', 
                 'box-shadow':'0 0 10px red',
                 'display':'flex',
                 'flex-direction':'column',
                 'align-items':'center',
                 'justify-content':'space-around'}, 
                {'position':'relative', 
                                    'left':'280px',
                                    'top':'25px'}]

if __name__ == '__main__':
    app.run_server(debug=True)