# Global Health and Economics Dashboard

This **Global Health and Economics Dashboard** is an interactive web application developed with **Dash and Plotly** that visualizes key global health and economic indicators, such as population, GDP per capita, and life expectancy, across different countries and years. The dashboard enables users to explore and analyze trends over time, offering valuable insights into how various factors impact the well-being and economic health of nations worldwide.

![image](https://github.com/user-attachments/assets/115e4ed9-cb8c-426f-99a6-e6d1560054bd)


## Features

- **Country and Metric Selection**: Choose any country and analyze various metrics, including population, GDP per capita, and life expectancy.
- **Time-Series Visualization**: Observe trends in the selected metric over time with interactive line charts.
- **Comparative Analysis**: Compare different metrics (e.g., population, GDP, life expectancy) side-by-side for a chosen country in the most recent available year using bar charts.
- **Responsive Layout**: Optimized for various screen sizes and devices, making it accessible from desktops, tablets, and mobile devices.

## Technology Stack

- **Dash** and **Plotly**: For building and visualizing the interactive web application.
- **Pandas**: For data manipulation and processing.
- **Data Source**: Sample data from Plotly's `gapminder_unfiltered.csv` dataset, representing various economic and health metrics from countries worldwide.

## Installation and Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Dawit-P/Global-Health-and-Economics-Dashboard-Using-Dash.git
   cd Global-Health-and-Economics-Dashboard-Using-Dash

2. **Install the required libraries**:

   ```bash
   pip install dash pandas plotly

3. **Run the app**:

   ```bash
   python app.py

4. **Access the dashboard**: Open http://127.0.0.1:8050 in your web browser.
   ```bash
   http://127.0.0.1:8050

Future Improvements
Data Filtering: Adding more filters such as continent and income groups.
Expanded Metrics: Including additional global health indicators.
Enhanced Data Sources: Integrating real-time data from public APIs for up-to-date insights.
