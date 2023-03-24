from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from dash_bootstrap_components.themes import CYBORG


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



if __name__ == '__main__':
    app.run_server(debug=True)