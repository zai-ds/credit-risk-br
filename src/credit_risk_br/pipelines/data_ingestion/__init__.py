from kedro.pipeline import Pipeline, node, pipeline
from .nodes.ingest_data import load_raw_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=load_raw_data,
            inputs="params:raw_data_path",
            outputs="raw_dataset",
            name="load_raw_data_node"
        )
    ])
