import pandas as pd
import numpy as np
import pickle
from xgboost import XGBClassifier
from typing import Tuple

class CreditRiskModel:
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.model = self._load_model()

    def _load_model(self) -> XGBClassifier:
        """Carrega o modelo treinado a partir do arquivo pickle."""
        with open(self.model_path, "rb") as f:
            model = pickle.load(f)
        return model

    def predict(self, data: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
        """
        Gera predições a partir dos dados recebidos.

        Args:
            data: DataFrame com as features.

        Returns:
            Tuple com:
                - predictions (0 ou 1)
                - probabilidades de inadimplência (float entre 0 e 1)
        """
        probas = self.model.predict_proba(data)[:, 1]
        preds = (probas >= 0.5).astype(int)
        return preds, probas
