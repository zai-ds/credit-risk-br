from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from credit_risk_br.pipelines import data_engineering as de
from credit_risk_br.pipelines import modeling as md

def register_pipelines() -> Dict[str, Pipeline]:
    data_engineering_pipeline = de.create_pipeline()
    modeling_pipeline = md.create_pipeline()

    return {
        "de": data_engineering_pipeline,
        "modeling": modeling_pipeline,
        "__default__": data_engineering_pipeline + modeling_pipeline,
    }
