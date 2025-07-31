import pandas as pd

def load_and_clean_data(raw_df: pd.DataFrame) -> pd.DataFrame:
    """Executa limpeza básica no dataset bruto."""
    df = raw_df.copy()
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df
