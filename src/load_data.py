from pathlib import Path
import pandas as pd


def load_raw_data(path: str | Path) -> pd.DataFrame:
    """
    Load the raw A/B test dataset from a CSV file.

    Parameters
    ----------
    path : str | Path
        Path to the raw CSV file.

    Returns
    -------
    pd.DataFrame
        Loaded raw dataset.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.
    ValueError
        If the loaded file is empty.
    """
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"Raw data file not found: {file_path}")

    df = pd.read_csv(file_path)

    if df.empty:
        raise ValueError(f"Loaded dataset is empty: {file_path}")

    return df