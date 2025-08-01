from kedro.pipeline import Pipeline, node, pipeline
from .nodes import calculate_shap_values, generate_shap_summary_plot

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=calculate_shap_values,
            inputs=["model", "X_test"],
            outputs="shap_values",
            name="calculate_shap_values_node"
        ),
        node(
            func=generate_shap_summary_plot,
            inputs=["shap_values", "X_test", "params:shap_plot_path"],
            outputs=None,
            name="generate_shap_summary_plot_node"
        ),
    ])
