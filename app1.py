# Imports
from dash import Dash, html, dcc, Input, Output

# App
app = Dash(__name__)
server = app.server
# Layout
app.layout = html.Div(children=[
    html.Div(
        dcc.RangeSlider(-5,6,1,id='slider',value=[1,2]),
        style=dict(width='50%')
    ),
    html.H1(id='out')
])

# Callbacks
@app.callback(
        Output('out','children'),
        Input('slider','value')
)
def callback(value):
    return value[0]*value[1]

# Server
if __name__ == "__main__":
    app.run_server(debug=True)