from dash import Dash, dcc, html, Input, Output,callback
app = Dash(__name__)
server = app.server
app.layout = html.Div([
    dcc.Dropdown(['blue','green','yellow'], id='color_dropdown'),
    html.Div(id='color_output')
])

@callback(
    Output('color_output', 'children'),
    Input('color_dropdown', 'value')
)
def update_output(value):
    return f'You have selected {value}'

if __name__ == '__main__':
    app.run(debug=True)
