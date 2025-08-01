from kedro.pipeline import Pipeline, node, pipeline
from .nodes import calculate_shap_values

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=calculate_shap_values,
            inputs=["model", "X_test"],
            outputs="shap_values",
            name="calculate_shap_values_node"
        )
    ])
