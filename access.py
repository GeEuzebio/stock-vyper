from dash import Dash, html, dcc, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
from dash_bootstrap_components.themes import CYBORG
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go


app = Dash(__name__, 
           external_stylesheets = [dbc.themes.BOOTSTRAP, CYBORG, '/assets/style.css'],
           suppress_callback_exceptions=True)

app.layout = dbc.Row(
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
                                        dbc.Input(id='end',type='date')],
                                                      style={'display':'flex', 
                                                             'align-items':'center'}),
                        html.Div([html.Div(id='grade',
                                         children=[], style={'margin-right':'5px',
                                                             'height':'450px',
                                                             'overflow-y':'scroll',
                                                             'border':'solid 0.5px #fff'}),
                                html.Div(id='graph',
                                         children=[], style={'margin-left':'5px'})], style={'display':'flex',
                                                               'align-items':'flex-start'}),
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
                        html.Div(id='candle-stick', children=[], style={'width':'85%',
                                                                        'margin-top':'15px',
                                                                        'border':'solid 0.5px #fff'})
                        ], style={'display':'flex',
                                  'flex-direction':'column',
                                  'align-items':'center'})
)

@app.callback(
        [Output('grade', 'children'),
         Output('graph', 'children'),
         Output('candle-stick', 'children')],
        [Input('input-ativo',  'value'),
         Input('start', 'value'),
         Input('end', 'value')],
        prevent_initial_call=True
)

def get_info(value, start, end):
        if not value:
            return html.Div("Por favor, digite um ativo válido na caixa de pesquisa.")
        
        ticker = yf.Ticker(value + '.SA')
        data = ticker.history(start=start, end=end)[["Open", "High", "Low", "Close"]]
        df = pd.DataFrame(data, columns=["Open", "High", "Low", "Close"])
        table = dash_table.DataTable(id='ativo-table',
                                             columns=[{'name': 'Open', 'id':'Open'},
                                             {'name': 'High', 'id':'High'},
                                             {'name': 'Low', 'id':'Low'},
                                             {'name': 'Close', 'id':'Close'},],
                                             data=df.round(2).to_dict('records'),
                                             style_table={
                                                'backgroundColor': '#000',
                                                'color':'#fff',
                                                 'text-align': 'center',
                                                 'width':'654px'
                                             },
                                             style_cell={
                                                'backgroundColor': '#000',
                                                'color': '#fff',
                                                 'text-align': 'center'
                                             },
                                             style_header={
                                                 'backgroundColor': '#ed1f34',
                                                 'fontWeight': 'bold',
                                                 'color': '#fff',
                                                 'text-align': 'center'
                                             })
        
        graph = dcc.Graph(
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
        style={'width':'654px',
               'heigh':'450px',
               'border':'solid 0.5px #fff',
               'border-radius':'5px'}
    ),
        candle = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'],
                                     close=df['Close'],
                                     high=df['High'],
                                     low=df['Low'])])
        candle.update_layout(title='Gráfico Candlestick',
                  yaxis_title='Preço',
                  xaxis_rangeslider_visible=False,
                  plot_bgcolor='black',
                  paper_bgcolor='black',
                  xaxis=dict(gridcolor='white'),
                  yaxis=dict(gridcolor='white'))

        return table, graph, dcc.Graph(figure=candle)


if __name__ == '__main__':
    app.run_server(debug=True)