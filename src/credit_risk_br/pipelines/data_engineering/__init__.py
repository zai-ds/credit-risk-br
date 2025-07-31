from kedro.pipeline import Pipeline
from .pipeline import create_pipeline

def register_pipelines() -> dict[str, Pipeline]:
    return {
        "data_engineering": create_pipeline(),
        "__default__": create_pipeline(),
    }
