import streamlit as st
from config import COLUMN_OPTIONS


def get_plot_parameters(data) -> dict:
    """
    Gather user input parameters from Streamlit sidebar.

    Parameters:
    - data: DataFrame used to infer min/max for axes and detection methods.

    Returns:
    - Dictionary with plotting configuration:
      x_axis, y_axis, color, marker_size, marker_style,
      log_scale, color_by, selected_methods, hover_data, solar_system.
    """
    st.sidebar.header("Plot Configuration")

    # initialize saved axis limits in session_state
    if 'saved_x_limits' not in st.session_state:
        st.session_state['saved_x_limits'] = None
    if 'saved_y_limits' not in st.session_state:
        st.session_state['saved_y_limits'] = None

    # Axis selectors
    x_display = st.sidebar.selectbox("X-axis", list(COLUMN_OPTIONS.keys()), index=0)
    y_display = st.sidebar.selectbox("Y-axis", list(COLUMN_OPTIONS.keys()), index=2)
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

    fixed_color = st.sidebar.color_picker("Point color", "#00f900")
    marker_size = st.sidebar.slider("Marker size", 0.1, 5.0, 1.0, 0.1)
    marker_opacity = st.sidebar.slider("Marker opacity", 0.0, 1.0, 0.5, 0.05)
    marker_style = st.sidebar.selectbox("Marker symbol", ['circle', 'square', 'diamond', 'star'])

    # Log scaling
    log_scale = st.sidebar.checkbox("Log scale axes", value=True)

    # Hover data fields
    hover_data = list(data.columns)

    # Solar system overlay
    solar_system = st.sidebar.checkbox("Overlay Solar System planets", value=True)

    return {
        "x_axis": x_axis,
        "y_axis": y_axis,
        "fixed_color": fixed_color,
        "marker_size": marker_size,
        "marker_style": marker_style,
        "log_scale": log_scale,
        "color_by": color_by,
        "selected_methods": selected_methods,
        "hover_data": hover_data,
        "solar_system": solar_system,
        "opacity": marker_opacity,
    }
