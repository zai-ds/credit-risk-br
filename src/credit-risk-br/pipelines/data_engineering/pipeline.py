from kedro.pipeline import Pipeline, node, pipeline
from .nodes import load_and_clean_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=load_and_clean_data,
            inputs="raw_dataset",
            outputs="preprocessed_dataset",
            name="load_and_clean_data_node",
        ),
    ])
