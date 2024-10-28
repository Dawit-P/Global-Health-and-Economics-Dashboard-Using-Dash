from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

# Load dataset
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

# Create Dash application
app = Dash(__name__)

# Application Layout
app.layout = html.Div(style={'backgroundColor': '#f9f9f9', 'fontFamily': 'Arial, sans-serif'}, children=[
    html.H1('Global Health and Economics Dashboard', style={'textAlign': 'center', 'color': '#4a4a4a'}),
    html.Div(
        children=[
            html.Label('Select Country:', style={'fontSize': '18px'}),
            dcc.Dropdown(id='country-dropdown', 
                         options=[{'label': country, 'value': country} for country in df.country.unique()],
                         value='Canada',
                         style={'width': '50%', 'margin': '0 auto', 'color': '#333'}
            ),
            html.Label('Select Metric:', style={'fontSize': '18px'}),
            dcc.RadioItems(
                id='metric-radio',
                options=[
                    {'label': 'Population', 'value': 'pop'},
                    {'label': 'GDP per Capita', 'value': 'gdpPercap'},
                    {'label': 'Life Expectancy', 'value': 'lifeExp'}
                ],
                value='pop',
                labelStyle={'display': 'inline-block', 'padding': '0 20px'},
                style={'textAlign': 'center', 'padding': '10px 0'}
            )
        ],
        style={'textAlign': 'center', 'padding': '20px', 'backgroundColor': '#e2e2e2', 'borderRadius': '5px', 'margin': '20px auto', 'width': '80%'}
    ),
    html.Div(children=[
        dcc.Graph(id='main-graph', config={'displayModeBar': False}),
        dcc.Graph(id='secondary-graph', config={'displayModeBar': False})
    ], style={'display': 'flex', 'justifyContent': 'space-around', 'padding': '20px'})
])
@callback(
    [Output('main-graph', 'figure'), Output('secondary-graph', 'figure')],
    [Input('country-dropdown', 'value'), Input('metric-radio', 'value')]
)
def update_graphs(selected_country, selected_metric):
    try:
        # Filter data by selected country
        dff = df[df['country'] == selected_country]

        # Main line chart: Trend over time of the selected metric
        fig_main = px.line(dff, x='year', y=selected_metric, title=f'{selected_metric} over Time in {selected_country}')
        fig_main.update_layout(title_font_size=18, plot_bgcolor='#f9f9f9', paper_bgcolor='#f9f9f9', title_x=0.5)

        # Secondary bar chart: Comparison of population, GDP, and life expectancy in the most recent year
        latest_year = dff['year'].max()
        recent_data = dff[dff['year'] == latest_year].melt(id_vars=['country', 'year'], value_vars=['pop', 'gdpPercap', 'lifeExp'], 
                                                           var_name='Metric', value_name='Value')
        fig_secondary = px.bar(
            recent_data,
            x='Metric',
            y='Value',
            title=f'Population, GDP per Capita, and Life Expectancy in {selected_country} ({latest_year})'
        )
        fig_secondary.update_layout(title_font_size=18, plot_bgcolor='#f9f9f9', paper_bgcolor='#f9f9f9', title_x=0.5)

        return fig_main, fig_secondary

    except Exception as e:
        print("Error:", e)
        return {}, {}  # Return empty figures on error

# Run application
if __name__ == '__main__':
    app.run_server(debug=True)

