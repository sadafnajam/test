import os
import plotly.express as px
import dash
from dash import html, dcc

app = dash.Dash()

df = px.data.iris() # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")


app = dash.Dash()
server = app.server 

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

print('This should test conda buildpack')

if __name__ == "__main__":
    app.run_server(debug=True)
