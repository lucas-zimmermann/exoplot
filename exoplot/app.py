import streamlit as st
from data_loader import load_exoplanet_data, load_solar_system_data
from sidebar import get_plot_parameters
from plotters import create_plotly_scatter, add_solar_system_trace
from streamlit_plotly_events import plotly_events
import os


st.set_page_config(layout="wide")

def main():
    """
    Entry point for the Streamlit Exoplanet Plotting App.

    Loads data, collects user inputs, filters by detection method,
    and renders an interactive Plotly scatter plot.
    """
    st.title("Exoplot: Interactive Exoplanet Plotting")

    # Load full dataset
    exo_data = load_exoplanet_data()

    # Sidebar parameters
    config = get_plot_parameters(exo_data)

    # Filter by detection method if requested
    if config['color_by'] == 'Discovery method' and config['selected_methods']:
        exo_data = exo_data[exo_data[config['color_by'] == 'Discovery method' and 'discoverymethod' or ''] .isin(config['selected_methods'])]

    # Build and show plot
    fig = create_plotly_scatter(exo_data, config)

    # Optional Solar System overlay
    if config['solar_system']:
        ss_data = load_solar_system_data()
        fig = add_solar_system_trace(fig, ss_data, config)


    # Update layout and display
    fig.update_layout(height=800)
    st.plotly_chart(fig, use_container_width=True)


if __name__ == '__main__':
    main()
