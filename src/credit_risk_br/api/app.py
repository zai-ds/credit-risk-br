from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
import pandas as pd

from credit_risk_br.api.model_loader import CreditRiskModel

# Inicializa a API e o modelo
app = FastAPI(title="Credit Risk API")
model = CreditRiskModel("data/06_models/model.pkl")

# Define o esquema de entrada esperado (ajuste as features conforme necessário)
class InputInstance(BaseModel):
    data: List[Dict[str, Any]]

# Endpoint de predição
@app.post("/predict")
def predict(input_data: InputInstance):
    try:
        df = pd.DataFrame(input_data.data)
        preds, probas = model.predict(df)

        results = [
            {"prediction": int(pred), "probability": float(prob)}
            for pred, prob in zip(preds, probas)
        ]
        return {"results": results}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
