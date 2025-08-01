from kedro.pipeline import Pipeline, node, pipeline
from credit_risk_br.pipelines.data_ingestion import nodes


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=nodes.load_raw_data,
                inputs=None,
                outputs="raw_dataset",
                name="ingest_data_node",
            ),
        ]
    )
