from dash import Dash, html, dcc, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
from dash_bootstrap_components.themes import CYBORG
import pandas as pd
import yfinance as yf


app = Dash(__name__, 
           external_stylesheets = [dbc.themes.BOOTSTRAP, CYBORG, '/assets/style.css'],
           suppress_callback_exceptions=True)

app.layout = dbc.Row(
                        dbc.Col([
                                html.Div([dbc.CardImg(src='/assets/img/vyper_logo_2.png',
                                                      style={'width':'100px'}),
                                          dbc.InputGroup([dbc.InputGroupText(html.Img(src="https://img.icons8.com/material-outlined/24/000000/search--v1.png")),
                                            dbc.Input(id='input-ativo',
                                                      placeholder='Digite o ativo',
                                                      style={'width':'200px'})],
                                                      className='mb-3')],
                                                      style={'display':'flex', 
                                                             'align-items':'center'}),
                                html.Div(id='grade',
                                         children=[]),
                                html.Div()
                        ], style={'display':'flex',
                                  'flex-direction':'column',
                                  'align-items':'center'})
)

@app.callback(
        Output('grade', 'children'),
        Input('input-ativo',  'value')
)

def get_info(value):
    if not value:
        return html.Div("Por favor, digite um ativo válido na caixa de pesquisa.")
    try:
        data = yf.download(value)[["Open", "High", "Low", "Close"]]
        df = pd.DataFrame(data, columns=["Open", "High", "Low", "Close"])
        table = dash_table.DataTable(columns=[{'name': 'Open', 'id':'Open'},
                                             {'name': 'High', 'id':'High'},
                                             {'name': 'Low', 'id':'Low'},
                                             {'name': 'Close', 'id':'Close'},],
                                             data=df.to_dict('records'))
        return table
    except:
        return html.Div("Desculpe, não foi possível encontrar informações para o ativo inserido. Por favor, tente novamente com um ativo válido.")

if __name__ == '__main__':
    app.run_server(debug=True)