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
                html.H1('Stock Vyper', id='vyper-h1', style={'color':'#ed1f34', 
                                              'text-align':'center',
                                              'padding':'0'}),
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
    allow_duplicate=True),
    Output('vyper-h1', 'style')],
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
                        html.Div([html.Div([
                            html.P('Usuário', style={'color':'#fff',
                                    'text-stroke':'1px #000'}),
                            dcc.Input(id='username',
                                    type='text',
                                    placeholder='Digite o usuário',
                                    autoComplete='username')], style={
                                    'display':'flex',
                                    'flex-direction':'column',
                                    'align-items':'flex-start'
                                    }),
                        html.Div([
                            html.P('Senha', style={'color':'#fff',
                                    'text-stroke':'1px #000'}),
                            dcc.Input(id='password',
                                    type='password',
                                    placeholder='Digite a senha',
                                    autoComplete='username')], style={
                                    'display':'flex',
                                    'flex-direction':'column',
                                    'align-items':'flex-start',
                                    'margin-top':'10px'
                                    })], style={'display':'flex', 'flex-direction':'column', 'margin-top':'20px'}),
                        html.Div([
                            dcc.Link('Esqueci a senha', href='#', style={'color':'#fff', 'text-stroke':'1px #000'}),
                            dbc.Button(
                                       children=[],
                                       id='login-button', 
                                       style={
                                              'background-color':'#ed1f34'},
                                       className = 'login-button',
                                       n_clicks=0),
                         ], 
                         style={'width':'100%',
                                'display':'flex', 
                                'align-items':'center', 
                                'justify-content':'space-around'}),
                                html.Div(id='loading', children=[])],
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
                                  'filter':'blur(5px)'}, {'color':'#ed1f34', 
                                              'text-align':'center',
                                              'padding':'0',
                                              'filter':'blur(5px)'}
    elif n_clicks == 0:
        return (html.Div(), {'width':'500px', 'filter':'none'}, {'width':'80px', 
                                  'height':'40px',
                                  'background-color':'#ed1f34'})
    
@app.callback(
    [Output('portal-div', 'style'),
     Output('close', 'style'),
     Output('vyper-img', 'style'),
     Output('entre', 'style'),
     Output('vyper-h1', 'style',
    allow_duplicate=True)],
    Input('close', 'n_clicks'),
    prevent_initial_call=True
)
def close_div(n_clicks):
    if n_clicks > 0:
        return [{'display': 'none'}, {'display': 'none'}, {'width':'500px', 'filter':'none'}, {'width':'80px', 
                                  'height':'40px',
                                  'background-color':'#ed1f34', 'filter':'none'},{'color':'#ed1f34', 
                                              'text-align':'center',
                                              'padding':'0'}]
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
                                  'filter':'blur(5px)'},{'color':'#ed1f34', 
                                              'text-align':'center',
                                              'padding':'0',
                                              'filter':'blur(5px)'}]
@app.callback(
    Output('login-button', 'n_clicks',
    allow_duplicate=True),
    [Input('login-button', 'n_clicks_timestamp'),
     Input('login-button', 'n_blur')],
    [State('login-button', 'n_clicks')],
    prevent_initial_call=True)
def captura_click_fora_botao(n_clicks_timestamp, n_blur, n_clicks):
    if n_clicks_timestamp is None:
        return 0
    elif n_clicks_timestamp is not None:
        return n_clicks
        

@app.callback(
    [Output('login-button', 'children'),
     Output('loading', 'children')],
    Input('login-button', 'n_clicks')
)

def state_button(n_clicks):
    if n_clicks>0:
        return [html.Img(src='/assets/img/check.png', style={'margin':'auto'}), html.Div( html.Div(className='circle-inner',style={'width':'45px',
                                            'height':'45px',
                                            'border':'solid 3px #000',
                                            'border-left-color':'red',
                                            'border-right-color':'red',
                                            'border-radius':'50%',
                                            'margin':'auto'}),
                                            className='circle',
                                            style={'width':'50px',
                                            'height':'50px',
                                            'border':'solid 3px #000',
                                            'border-top-color':'red',
                                            'border-bottom-color':'red',
                                            'border-radius':'50%'})]
    elif n_clicks==0:
        return [html.P('Login', style={'margin':'auto'}), html.Div()]
    


if __name__ == '__main__':
    app.run_server(debug=True)