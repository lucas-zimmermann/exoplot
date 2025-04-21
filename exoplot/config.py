
# Mapping of display names to actual column names in the dataset
COLUMN_OPTIONS = {
    "Orbital Period": "pl_orbper",
    "Orbital Semi-Major Axis": "pl_orbsmax",
    "Planetary Radius": "pl_rade",
    "Planetary Mass": "pl_bmasse",
    "Orbital Eccentricity": "pl_orbeccen",
}

# Inverted for display purposes
DISPLAY_FOR = {col: disp for disp, col in COLUMN_OPTIONS.items()}

# Unit mapping for axis labels
UNIT_MAPPING = {
    'pl_orbper': 'days',
    'pl_orbsmax': 'au',
    'pl_rade': 'Earth radii',
    'pl_bmasse': 'Earth masses',
    'pl_orbeccen': ''
}