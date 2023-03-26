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
     Output('vyper-img', 'style',
    allow_duplicate=True),
     Output('entre', 'style',
    allow_duplicate=True)],
    Input('entre', 'n_clicks'),
    prevent_initial_call=True
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
                        html.Div([
                            html.P('Usuário', style={'color':'#fff'}),
                            dcc.Input(id='username',
                                    type='text',
                                    placeholder='Digite o usuário',
                                    autoComplete='username')], style={
                                    'display':'flex',
                                    'flex-direction':'column',
                                    'align-items':'flex-start'
                                    }),
                        html.Div([
                            html.P('Senha', style={'color':'#fff'}),
                            dcc.Input(id='password',
                                    type='password',
                                    placeholder='Digite a senha',
                                    autoComplete='username')], style={
                                    'display':'flex',
                                    'flex-direction':'column',
                                    'align-items':'flex-start'
                                    }),
                        html.Div([
                            dcc.Link('Esqueci a senha', href='#', style={'color':'#fff'}),
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
                                    'display':'flex',
                                    'flex-direction':'column',
                                    'align-items':'center',
                                    'justify-content':'space-around'},
                            id='portal-div')
                ], style={'position':'absolute',
                          'left':'40.2%',
                          'top':'100px'}), {'width':'500px',
                          'filter':'blur(5px)'}, {'width':'80px', 
                                  'height':'40px',
                                  'background-color':'#ed1f34',
                                  'filter':'blur(5px)'}
    elif n_clicks == 0:
        return (html.Div(), {'width':'500px', 'filter':'none'}, {'width':'80px', 
                                  'height':'40px',
                                  'background-color':'#ed1f34'})
    
@app.callback(
    [Output('portal-div', 'style'),
     Output('close', 'style'),
     Output('vyper-img', 'style'),
     Output('entre', 'style')],
    Input('close', 'n_clicks')
)
def close_div(n_clicks):
    if n_clicks > 0:
        return [{'display': 'none'}, {'display': 'none'}, {'width':'500px', 'filter':'none'}, {'width':'80px', 
                                  'height':'40px',
                                  'background-color':'#ed1f34', 'filter':'none'}]
    else:
        return [{'width':'300px', 
                 'height':'400px',
                 'display':'flex',
                 'flex-direction':'column',
                 'align-items':'center',
                 'justify-content':'space-around'}, 
                {'position':'relative', 
                                    'left':'280px',
                                    'top':'25px'},
                      {'width':'500px', 'filter':'blur(5px)'}, {'width':'80px', 
                                  'height':'40px',
                                  'background-color':'#ed1f34',
                                  'filter':'blur(5px)'}]

if __name__ == '__main__':
    app.run_server(debug=True)