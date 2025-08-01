import pandas as pd
from pathlib import Path
from typing import Tuple

def load_raw_data(data_path: str) -> pd.DataFrame:
    """
    Carrega os dados brutos a partir de um CSV local.

    Args:
        data_path: Caminho para o arquivo CSV.

    Returns:
        DataFrame contendo os dados brutos.
    """
    path = Path(data_path)
    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {data_path}")
    
    df = pd.read_csv(path)
    return df
