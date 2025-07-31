from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

def register_pipelines() -> dict[str, Pipeline]:
    from bank_credit_scoring.pipelines.data_ingestion import create_pipeline as create_ingestion_pipeline

    ingestion_pipeline = create_ingestion_pipeline()

    return {
        "data_ingestion": ingestion_pipeline,
        "__default__": ingestion_pipeline,
    }
