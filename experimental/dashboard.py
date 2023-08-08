import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

# Create a dictionary with data
data = {
    'continent': ['Asia', 'Europe', 'Africa', 'Asia', 'Europe', 'Africa'] * 4,
    'country': ['China', 'France', 'Nigeria', 'Japan', 'Germany', 'Egypt'] * 4,
    'gdpPercap': np.random.randint(5000, 45000, size=24),
    'year': [2020, 2020, 2020, 2020, 2020, 2020, 2021, 2021, 2021, 2021, 2021, 2021, 2022, 2022, 2022, 2022, 2022, 2022, 2023, 2023, 2023, 2023, 2023, 2023]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Initialize the app
app = dash.Dash(__name__)

# Define the app
app.layout = html.Div([
    html.H1("Country GDP Dashboard"),
    
    dcc.Dropdown(
        id='continent-dropdown',
        options=[{'label': i, 'value': i} for i in df['continent'].unique()],
        value='Asia'
    ),
    
    dcc.Dropdown(
        id='country-dropdown'
    ),
    
    dcc.Graph(
        id='gdp-graph'
    )
])

@app.callback(
    Output('country-dropdown', 'options'),
    Input('continent-dropdown', 'value'))
def update_country_dropdown(selected_continent):
    filtered_df = df[df['continent'] == selected_continent]
    return [{'label': i, 'value': i} for i in filtered_df['country'].unique()]

@app.callback(
    Output('gdp-graph', 'figure'),
    Input('continent-dropdown', 'value'),
    Input('country-dropdown', 'value'))
def update_graph(selected_continent, selected_country):
    filtered_df = df[(df['continent'] == selected_continent) & (df['country'] == selected_country)]
    return px.line(filtered_df, x='year', y='gdpPercap', title=f'GDP Per Capita for {selected_country}')

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
