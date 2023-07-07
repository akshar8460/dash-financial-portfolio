import pandas as pd
import plotly.graph_objects as go
from dash import Dash, html, dash_table, dcc

# Load portfolio data from CSV
portfolio_data = pd.read_csv('portfolio.csv')

# Calculate portfolio value
portfolio_data['Value'] = portfolio_data['Quantity'] * portfolio_data['Purchase Price']

# Set up pagination
PAGE_SIZE = 10  # Number of rows to display per page

# Initialize the Dash application
app = Dash(__name__)

# Define the layout of the application
app.layout = html.Div(
    children=[
        html.H1('Dash Financial Portfolio'),

        dcc.Graph(
            figure=go.Figure(
                data=[
                    go.Pie(
                        labels=portfolio_data['Stock Symbol'],
                        values=portfolio_data['Value'],
                        textinfo='label+percent',
                        insidetextorientation='radial',
                    ),
                ],
                layout=go.Layout(
                    title='Portfolio Composition',
                )
            )
        ),

        dash_table.DataTable(
            id='portfolio-table',
            columns=[
                {'name': 'Stock Symbol', 'id': 'Stock Symbol'},
                {'name': 'Quantity', 'id': 'Quantity'},
                {'name': 'Purchase Price', 'id': 'Purchase Price'},
                {'name': 'Value', 'id': 'Value'},
            ],
            data=portfolio_data.to_dict('records'),
            page_size=PAGE_SIZE,
            style_table={'overflowX': 'auto'},
            style_data={'whiteSpace': 'normal', 'height': 'auto'},
            style_cell={'textAlign': 'left'},
        )
    ]
)

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
