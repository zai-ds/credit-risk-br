import pandas as pd
import shap
import numpy as np
from xgboost import XGBClassifier

def calculate_shap_values(model: XGBClassifier, X_test: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula os valores SHAP para o modelo treinado com base em X_test.

    Args:
        model: Modelo treinado (XGBoost).
        X_test: Dados de teste.

    Returns:
        DataFrame com valores SHAP por instância e feature.
    """
    explainer = shap.Explainer(model)
    shap_values = explainer(X_test)

    shap_df = pd.DataFrame(shap_values.values, columns=X_test.columns, index=X_test.index)
    return shap_df
