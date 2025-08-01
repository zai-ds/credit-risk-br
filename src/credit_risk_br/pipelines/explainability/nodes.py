import pandas as pd
import shap
import matplotlib.pyplot as plt
from xgboost import XGBClassifier

def calculate_shap_values(model: XGBClassifier, X_test: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula os valores SHAP para o modelo treinado com base em X_test.
    """
    explainer = shap.Explainer(model)
    shap_values = explainer(X_test)
    shap_df = pd.DataFrame(shap_values.values, columns=X_test.columns, index=X_test.index)
    return shap_df

def generate_shap_summary_plot(shap_values: pd.DataFrame, X_test: pd.DataFrame, output_path: str) -> None:
    """
    Gera e salva o gráfico summary plot dos valores SHAP.

    Args:
        shap_values: DataFrame com os valores SHAP.
        X_test: Dados de teste.
        output_path: Caminho do arquivo .png de saída.
    """
    plt.figure(figsize=(10, 6))
    shap.summary_plot(shap_values.values, features=X_test, feature_names=X_test.columns, show=False)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
