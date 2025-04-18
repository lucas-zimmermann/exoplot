
import streamlit as st
import math
from config import COLUMN_OPTIONS


def get_plot_parameters(data) -> dict:
    """
    Gather user input parameters from Streamlit sidebar.

    Parameters:
    - data: DataFrame used to infer min/max for axes and detection methods.

    Returns:
    - Dictionary with plotting configuration:
      x_axis, y_axis, color, marker_size, marker_style,
      use_custom_limits, x_limits, y_limits, log_scale,
      color_by, selected_methods, hover_data, solar_system.
    """
    st.sidebar.header("Plot Configuration")

    # Axis selectors
    x_display = st.sidebar.selectbox("X-axis", list(COLUMN_OPTIONS.keys()))
    y_display = st.sidebar.selectbox("Y-axis", list(COLUMN_OPTIONS.keys()))
    x_axis = COLUMN_OPTIONS[x_display]
    y_axis = COLUMN_OPTIONS[y_display]

    # Discovery method filtering & coloring
    color_by = st.sidebar.selectbox(
        "Color points by", ["Fixed color", "Discovery method"]
    )
    selected_methods = None
    if color_by == "Discovery method":
        methods = sorted(data['discoverymethod'].dropna().unique())
        selected_methods = st.sidebar.multiselect(
            "Select detection methods to include", methods, default=methods
        )

    # Fixed color and markers
    fixed_color = st.sidebar.color_picker("Point color", "#00f900")
    marker_size = st.sidebar.slider("Marker size", 0.1, 5.0, 1.0, 0.1)
    marker_style = st.sidebar.selectbox("Marker symbol", ['o', 's', 'D', '*'])

    # Axis limits options
    use_custom_limits = st.sidebar.checkbox("Custom axis limits", value=False)
    if use_custom_limits:
        x_min = max(data[x_axis].min(), 0.1)
        x_max = data[x_axis].max()
        y_min = max(data[y_axis].min(), 0.1)
        y_max = data[y_axis].max()

        log_x_min, log_x_max = math.log10(x_min), math.log10(x_max)
        log_y_min, log_y_max = math.log10(y_min), math.log10(y_max)

        x_log_range = st.sidebar.slider(
            "X-axis log range",
            min_value=log_x_min,
            max_value=log_x_max,
            value=(log_x_min, log_x_max)
        )
        y_log_range = st.sidebar.slider(
            "Y-axis log range",
            min_value=log_y_min,
            max_value=log_y_max,
            value=(log_y_min, log_y_max)
        )

        x_limits = (10 ** x_log_range[0], 10 ** x_log_range[1])
        y_limits = (10 ** y_log_range[0], 10 ** y_log_range[1])
    else:
        x_limits, y_limits = None, None

    # Log scaling
    log_scale = st.sidebar.checkbox("Log scale axes", value=True)

    # Hover data fields
    show_all = st.sidebar.checkbox("Show all data on hover", value=True)
    if show_all:
        hover_data = list(data.columns)
    else:
        defaults = ['pl_name', x_axis, y_axis,  'discoverymethod']
        hover_data = st.sidebar.multiselect(
            "Hover fields", list(data.columns), default=[c for c in defaults if c in data.columns]
        )

    # Solar system overlay
    solar_system = st.sidebar.checkbox("Overlay Solar System planets", value=True)

    return {
        "x_axis": x_axis,
        "y_axis": y_axis,
        "fixed_color": fixed_color,
        "marker_size": marker_size,
        "marker_style": marker_style,
        "use_custom_limits": use_custom_limits,
        "x_limits": x_limits,
        "y_limits": y_limits,
        "log_scale": log_scale,
        "color_by": color_by,
        "selected_methods": selected_methods,
        "hover_data": hover_data,
        "solar_system": solar_system,
    }
