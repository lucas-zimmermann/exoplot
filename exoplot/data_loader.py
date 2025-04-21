import pandas as pd


def load_exoplanet_data(filepath: str = 'exoplot/exoplanet_archive.csv', comment: str = '#') -> pd.DataFrame:
    """
    Load exoplanet data from a CSV file.

    Parameters:
    - filepath: Path to the CSV file.
    - comment: Character indicating comment lines in CSV.

    Returns:
    - DataFrame with exoplanet data.
    """
    return pd.read_csv(filepath, comment=comment)


def load_solar_system_data(filepath: str = 'exoplot/solar_system.csv') -> pd.DataFrame:
    """
    Load solar system planet data from a CSV file.

    Parameters:
    - filepath: Path to the CSV file.

    Returns:
    - DataFrame with solar system planet data.
    """
    return pd.read_csv(filepath)