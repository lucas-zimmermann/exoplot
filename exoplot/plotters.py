import plotly.express as px
from config import DISPLAY_FOR, UNIT_MAPPING


DISPLAY_FOR.update({
    'pl_name': 'Planet Name',
    'discoverymethod': 'Discovery Method'
})



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
        opacity=config['opacity'],
        size_max=config['marker_size'] * 10,
        title=f"{DISPLAY_FOR.get(config['x_axis'], config['x_axis'])} vs {DISPLAY_FOR.get(config['y_axis'], config['y_axis'])}",
        labels={
            config['x_axis']: (
                f"{DISPLAY_FOR.get(config['x_axis'], config['x_axis'])}"
                + (f" ({UNIT_MAPPING[config['x_axis']]})"
                   if UNIT_MAPPING.get(config['x_axis']) else "")
            ),
            config['y_axis']: (
                f"{DISPLAY_FOR.get(config['y_axis'], config['y_axis'])}"
                + (f" ({UNIT_MAPPING[config['y_axis']]})"
                   if UNIT_MAPPING.get(config['y_axis']) else "")
            ),
            'pl_name': DISPLAY_FOR['pl_name'],
            'discoverymethod': DISPLAY_FOR['discoverymethod']
        }

    )
    fig.update_layout(title_x=0.35) # Center the title
    fig.update_yaxes(showgrid=False) # Hide y-axis grid lines

    # Apply marker symbol and size
    symbol = config['marker_style']
    fig.update_traces(
        marker=dict(size=config['marker_size'] * 10, symbol=symbol),
        selector=dict(mode='markers')
    )

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
    scatter = px.scatter(
        ss_data,
        x=config['x_axis'],
        y=config['y_axis'],
        hover_name='pl_name',
        text='pl_name',
        labels=DISPLAY_FOR,
        color_discrete_sequence=['orange'],
        size_max=config['marker_size'] * 10
    )
    scatter.update_traces(textposition='top center', mode='markers+text')
    scatter.update_traces(
        mode='markers+text',
        textposition='top center',
        textfont=dict(color='black', size=12),
        texttemplate='<b>%{text}</b>',
        marker=dict(opacity=0.7),

    )
    fig.add_traces(scatter.data)
    return fig