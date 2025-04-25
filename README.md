# Exoplot: Interactive Exoplanet Plotting

**Exoplot** is a Streamlit application that provides an interactive scatter‐plot visualization of exoplanet data from the NASA Exoplanet Archive, with optional overlay of Solar System planets. Users can:

- Select any two planet parameters (period, semi‑major axis, radius, mass, eccentricity) for the X and Y axes.
- Color points by discovery method or choose a fixed color.
- Adjust marker size, symbol, and opacity.
- Zoom and pan the Plotly chart and save your zoomed view as custom axes.
- View detailed hover tooltips (planet name, orbital and physical properties).

---

## Features

- **Dynamic Axis Selection**  
  Choose from orbital period, semi‑major axis, planetary radius, mass, or eccentricity.
- **Color & Style Controls**  
  Toggle between fixed color or discovery‑method grouping; pick marker size, symbol, and opacity.
- **Solar System Overlay**  
  Optionally show the eight Solar System planets in “orange” for comparison.
- **Interactive Plot**  
  Pan, zoom, and hover for details; save your viewport as the “current axes” so it persists across sidebar updates.
- **Human‑Friendly Labels**  
  Axis titles and tooltips show real names and units (e.g. “Orbital Period (days)”, “Planetary Mass (Earth masses)”).

---

## Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/lucas-zimmermann/Exoplot.git
   cd Exoplot
