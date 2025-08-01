from typing import Dict
from kedro.pipeline import Pipeline
from credit_risk_br.pipelines import data_ingestion as di
from credit_risk_br.pipelines import data_engineering as de
from credit_risk_br.pipelines import modeling as md
from credit_risk_br.pipelines import explainability as ex

def register_pipelines() -> Dict[str, Pipeline]:
    data_ingestion_pipeline = di.create_pipeline()
    data_engineering_pipeline = de.create_pipeline()
    modeling_pipeline = md.create_pipeline()
    explainability_pipeline = ex.create_pipeline()

    return {
        "di": data_ingestion_pipeline,
        "de": data_engineering_pipeline,
        "modeling": modeling_pipeline,
        "ex": explainability_pipeline,
        "__default__": (
            data_ingestion_pipeline +
            data_engineering_pipeline +
            modeling_pipeline +
            explainability_pipeline
        ),
    }
