import plotly.express as px
from config import COLUMN_OPTIONS


# Mapping from Matplotlib symbols to Plotly symbols
MATPLOT_TO_PLOTLY = {
    'o': 'circle',
    's': 'square',
    'D': 'diamond',
    '*': 'star'
}

DISPLAY_FOR = {col: disp for disp, col in COLUMN_OPTIONS.items()}


def create_plotly_scatter(data, config) -> px.scatter:
    """
    Create a Plotly scatter plot according to the provided configuration.

    Parameters:
    - data: DataFrame containing the data to plot.
    - config: Dictionary with plotting settings from sidebar.

    Returns:
    - Plotly Figure object.
    """



    # Create scatter plot
    fig = px.scatter(
        data,
        x=config['x_axis'],
        y=config['y_axis'],
        hover_name='pl_name',
        color_discrete_sequence=[config['fixed_color']] if config['color_by'] == 'Fixed color' else None,
        color='discoverymethod' if config['color_by'] == 'Discovery method' else None,
        size_max=config['marker_size'] * 10

    )
    fig.update_yaxes(showgrid=False)

    # Apply marker symbol and size
    symbol = MATPLOT_TO_PLOTLY.get(config['marker_style'], 'circle')
    fig.update_traces(
        marker=dict(size=config['marker_size'] * 10, symbol=symbol),
        selector=dict(mode='markers')
    )

    # Axis limits
    if config['use_custom_limits']:
        if config['x_limits']:
            fig.update_xaxes(range=config['x_limits'])
        if config['y_limits']:
            fig.update_yaxes(range=config['y_limits'])

    # Log scaling
    if config['log_scale']:
        if config['x_axis'] != 'pl_orbeccen':
            fig.update_xaxes(type='log')
        if config['y_axis'] != 'pl_orbeccen':
            fig.update_yaxes(type='log')

    # Clamp eccentricity
    if config['x_axis'] == 'pl_orbeccen':
        fig.update_xaxes(range=[0, 1])
    if config['y_axis'] == 'pl_orbeccen':
        fig.update_yaxes(range=[0, 1])

    return fig


def add_solar_system_trace(fig, ss_data, config):
    """
    Overlay Solar System planet data on an existing Plotly figure.

    Parameters:
    - fig: Plotly Figure to add traces to.
    - ss_data: DataFrame with solar system data (including 'pl_name').
    - config: Plot configuration dict (for axis keys, size).

    Returns:
    - Plotly Figure with additional traces.
    """
    trace = px.scatter(
        ss_data,
        x=config['x_axis'],
        y=config['y_axis'],
        hover_name='pl_name',
        color_discrete_sequence=['orange'],
        size_max=config['marker_size'] * 10
    ).data
    fig.add_traces(trace)
    return fig