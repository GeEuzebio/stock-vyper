from dash import Dash, html, dcc, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
from dash_bootstrap_components.themes import CYBORG
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import os

port = int(os.environ.get("PORT", 5000))

app = Dash(__name__, external_stylesheets = [CYBORG, '/assets/style.css'], suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

login_layout = dbc.Row(
        dbc.Col([
            dbc.Row([
                html.Img(src='/assets/img/vyper_logo_1.png', 
                         style={'width':'500px'},
                         id='vyper-img'),
                html.H3('Stock Vyper', id='vyper-h1', style={'color':'#ed1f34', 
                                              'text-align':'center',
                                              'padding':'0'}),
                html.H1('Predict the market', className='typing-text'),
                dbc.Button('Entre', 
                           id='entre',
                           n_clicks=0, 
                           style={'width':'80px', 
                                  'height':'40px',
                                  'background-color':'#ed1f34'},
                           className = 'button'),
                html.Div(children=[], id='login-popup'),
                html.Div(html.Img(src='/assets/img/shopping-cart.png'), 
                         style={'width':'60px',
                                'height':'60px',
                                'border-radius':'50%',
                                'background-image':'radial-gradient(farthest-corner,#ed1f34, #000)',
                                'position':'absolute',
                                'left':'10px',
                                'bottom':'140px',
                                'display':'flex',
                                'justify-content':'center',
                                'align-items':'center'}),
                html.Div(html.Img(src='/assets/img/instagram.png'), 
                         style={'width':'60px',
                                'height':'60px',
                                'border-radius':'50%',
                                'background-image':'linear-gradient(to bottom, #405de6, #5851db, #833ab4, #c13584, #e1306c, #fd1d1d)',
                                'position':'absolute',
                                'left':'10px',
                                'bottom':'50px',
                                'display':'flex',
                                'justify-content':'center',
                                'align-items':'center'}),
                html.Div(
                         [
                            html.P('Pt', style={'padding':'0'}),
                            html.Div(html.Div(id='switch',
                                              style={'border-radius':'50%',
                                                     'width':'10px',
                                                     'height':'10px',
                                                     'background-color':'red',
                                                     'position':'absolute'},
                                              className='switch',
                                              n_clicks=0),
                                              style={'height':'12px',
                                                     'margin':'0 10px',
                                                     'width':'25px',
                                                     'background-color':'#fff',
                                                     'border-radius':'20px',
                                                     'display':'flex',
                                                     'flex-direction':'column',
                                                     'justify-content':'center',
                                                     'box-content':'border-box'}),
                            html.P('En', style={'padding':'0'})
                         ],
                         style={'position':'fixed',
                                'left':'20px',
                                'top':'20px',
                                'display': 'flex',
                                'align-items':'center'}
                )
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
                            dcc.Link(dbc.Button(
                                       children=[],
                                       id='login-button', 
                                       style={
                                              'background-color':'#ed1f34'},
                                       className = 'login-button',
                                       n_clicks=0),
                                       href='/index'),
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
           
@app.callback(
    Output('switch', 'style'),
    Input('switch', 'n_clicks')
)

def switch(n_clicks):
    if n_clicks%2==1:
        return {'border-radius':'50%',
                'width':'10px',
                'height':'10px',
                'background-color':'red',
                'position':'absolute',
                'left':'51px'}
    else:
        return {'border-radius':'50%',
                'width':'10px',
                'height':'10px',
                'background-color':'red',
                'position':'absolute',
                'left':'41px'}
    
portal_layout = dbc.Row(
                        dbc.Col([
                                html.Div([dbc.CardImg(src='/assets/img/vyper_logo_2.png',
                                                      style={'width':'100px'}),
                                        html.Div([html.Img(src="https://img.icons8.com/material-outlined/24/000000/search--v1.png",
                                                           style={'position':'relative', 'left':'30px'}),
                                                  dbc.Input(id='input-ativo',
                                                                type='text',
                                                                placeholder='Digite o ativo',
                                                                style={'width':'200px',
                                                                       'padding-left':'35px',
                                                                       'margin-right':'10px'})],
                                                                style={'display':'flex',
                                                                       'align-items':'center',
                                                                       'padding':'0'}),
                                        dbc.Label('Data Inicial:', style={'margin':'5px'}),
                                        dbc.Input(id='start',type='date', style={'margin':'10px'}),
                                        dbc.Label('Data Final:', style={'margin':'5px'}),
                                        dbc.Input(id='end',type='date'),
                                        dcc.Dropdown(id='type-graph',options=['line', 'candle'], value='line', 
                                         style={'position':'relative',
                                                'left':'20px',
                                                'width':'100px'})],
                                                      style={'display':'flex', 
                                                             'align-items':'center'}),
                               html.Div([ html.Div(id='graph',
                                         children=[], style={'width':'85%'}),
                                         ],
                                                style={'width':'100%',
                                                       'margin':'auto',
                                                       'display':'flex',
                                                       'justify-content':'center'}),
                        html.Div([
                                html.Div([
                                        html.Div('Point 1',
                                                 style={'background-color':'#ed1f34',
                                                        'border':'solid 0.5px #ed1f34',
                                                        'border-bottom':'none',
                                                        'border-radius':'5px 5px 0 0',
                                                        'width':'100px',
                                                        'height':'30px',
                                                        'margin':'0',
                                                        'text-align':'center'}),
                                        html.Div(style={'background-color':'#000',
                                                        'border':'solid 0.5px #ed1f34',
                                                        'border-top':'none',
                                                        'border-radius':'0 0 5px 5px',
                                                        'width':'100px',
                                                        'height':'30px',
                                                        'margin':'0'})
                                ]),
                                html.Div([
                                        html.Div('Point 2', 
                                                 style={'background-color':'#ed1f34',
                                                        'border':'solid 0.5px #ed1f34',
                                                        'border-bottom':'none',
                                                        'border-radius':'5px 5px 0 0',
                                                        'width':'100px',
                                                        'height':'30px',
                                                        'margin':'0',
                                                        'text-align':'center'}),
                                        html.Div(style={'background-color':'#000',
                                                        'border':'solid 0.5px #ed1f34',
                                                        'border-top':'none',
                                                        'border-radius':'0 0 5px 5px',
                                                        'width':'100px',
                                                        'height':'30px',
                                                        'margin':'0'})
                                ]),
                                html.Div([
                                        html.Div('Point 3', 
                                                 style={'background-color':'#ed1f34',
                                                        'border':'solid 0.5px #ed1f34',
                                                        'border-bottom':'none',
                                                        'border-radius':'5px 5px 0 0',
                                                        'width':'100px',
                                                        'height':'30px',
                                                        'margin':'0',
                                                        'text-align':'center'}),
                                        html.Div(style={'background-color':'#000',
                                                        'border':'solid 0.5px #ed1f34',
                                                        'border-top':'none',
                                                        'border-radius':'0 0 5px 5px',
                                                        'width':'100px',
                                                        'height':'30px',
                                                        'margin':'0'})
                                ]),
                                html.Div([
                                        html.Div('Point 4', 
                                                 style={'background-color':'#ed1f34',
                                                        'border':'solid 0.5px #ed1f34',
                                                        'border-bottom':'none',
                                                        'border-radius':'5px 5px 0 0',
                                                        'width':'100px',
                                                        'height':'30px',
                                                        'margin':'0',
                                                        'text-align':'center'}),
                                        html.Div(style={'background-color':'#000',
                                                        'border':'solid 0.5px #ed1f34',
                                                        'border-top':'none',
                                                        'border-radius':'0 0 5px 5px',
                                                        'width':'100px',
                                                        'height':'30px',
                                                        'margin':'0'})
                                ]),
                                html.Div([
                                        html.Div('Point 5', 
                                                 style={'background-color':'#ed1f34',
                                                        'border':'solid 0.5px #ed1f34',
                                                        'border-bottom':'none',
                                                        'border-radius':'5px 5px 0 0',
                                                        'width':'100px',
                                                        'height':'30px',
                                                        'margin':'0',
                                                        'text-align':'center'}),
                                        html.Div(style={'background-color':'#000',
                                                        'border':'solid 0.5px #ed1f34',
                                                        'border-top':'none',
                                                        'border-radius':'0 0 5px 5px',
                                                        'width':'100px',
                                                        'height':'30px',
                                                        'margin':'0'})
                                ]),
                                html.Div([
                                        html.Div('Point 6',
                                                 style={'background-color':'#ed1f34',
                                                        'border':'solid 0.5px #ed1f34',
                                                        'border-bottom':'none',
                                                        'border-radius':'5px 5px 0 0',
                                                        'width':'100px',
                                                        'height':'30px',
                                                        'margin':'0',
                                                        'text-align':'center'}),
                                        html.Div(style={'background-color':'#000',
                                                        'border':'solid 0.5px #ed1f34',
                                                        'border-top':'none',
                                                        'border-radius':'0 0 5px 5px',
                                                        'width':'100px',
                                                        'height':'30px',
                                                        'margin':'0'})
                                ]),
                                html.Div([
                                        html.Div('Point 7',
                                                 style={'background-color':'#ed1f34',
                                                        'border':'solid 0.5px #ed1f34',
                                                        'border-bottom':'none',
                                                        'border-radius':'5px 5px 0 0',
                                                        'width':'100px',
                                                        'height':'30px',
                                                        'margin':'0',
                                                        'text-align':'center'}),
                                        html.Div(style={'background-color':'#000',
                                                        'border':'solid 0.5px #ed1f34',
                                                        'border-top':'none',
                                                        'border-radius':'0 0 5px 5px',
                                                        'width':'100px',
                                                        'height':'30px',
                                                        'margin':'0'})
                                ]),
                                html.Div([
                                        html.Div('Point 8',
                                                 style={'background-color':'#ed1f34',
                                                        'border':'solid 0.5px #ed1f34',
                                                        'border-bottom':'none',
                                                        'border-radius':'5px 5px 0 0',
                                                        'width':'100px',
                                                        'height':'30px',
                                                        'margin':'0',
                                                        'text-align':'center'}),
                                        html.Div(style={'background-color':'#000',
                                                        'border':'solid 0.5px #ed1f34',
                                                        'border-top':'none',
                                                        'border-radius':'0 0 5px 5px',
                                                        'width':'100px',
                                                        'height':'30px',
                                                        'margin':'0'})
                                ])
                        ], style={'width':'80%','display':'flex', 
                                  'align-items':'center', 
                                  'justify-content':'space-between', 
                                  'margin-top':'15px'}),
                        ], style={'display':'flex',
                                  'flex-direction':'column',
                                  'align-items':'center'})
)

@app.callback(
        Output('graph', 'children'),
        [Input('input-ativo',  'value'),
         Input('start', 'value'),
         Input('end', 'value'),
         Input('type-graph', 'value')],
        prevent_initial_call=True
)

def get_info(value, start, end, type): 
    ticker = yf.Ticker(value + '.SA')
    data = ticker.history(start=start, end=end)[["Open", "High", "Low", "Close"]]
    df = pd.DataFrame(data, columns=["Open", "High", "Low", "Close"])
    
    line = dcc.Graph(
    id='graph-plot',
    figure={
        'data': [
            {'x': df.index, 'y': df['Open'], 'type': 'line', 'name': 'Open Price'},
            {'x': df.index, 'y': df['High'], 'type': 'line', 'name': 'High Price'},
            {'x': df.index, 'y': df['Low'], 'type': 'line', 'name': 'Low Price'},
            {'x': df.index, 'y': df['Close'], 'type': 'line', 'name': 'Close Price'}
        ],
        'layout':{
            'title': f'Informações do ativo {value.upper()}',
            'plot_bgcolor':'#000',
            'paper_bgcolor':'#000',
            'lines':'#fff',
            'color':'#fff'
        }
    },
    ),
    candle = dcc.Graph(figure=go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'],
                                 close=df['Close'],
                                 high=df['High'],
                                 low=df['Low'])]))
    
    """candle.update_layout(title='Gráfico Candlestick',
              yaxis_title='Preço',
              xaxis_rangeslider_visible=False,
              plot_bgcolor='black',
              paper_bgcolor='black',
              xaxis=dict(gridcolor='white'),
              yaxis=dict(gridcolor='white'))"""
    if type == 'line':
        return line
    elif type == 'candle':
        return candle
    else:
        return line

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return login_layout
    elif pathname == '/index':
        return portal_layout

if __name__ == '__main__':
    #app.run_server(host='0.0.0.0', port=port)
    app.run_server(debug=True)