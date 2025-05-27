from airflow.decorators import dag,task
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from pendulum import datetime

URI="gs://terraform-basics-458014-movielens/movie_lens/tags.csv"

project_name="terraform-basics-458014"
dataset_name="movie_lens"
table_name="raw_tags"
conn_id="gcp"

@dag(
    start_date=datetime(2025,5,25),
    schedule=None,
    catchup=False,
    tags=['ingest_tags']
)

def ingest_tags_to_bq():
    run_tags_ingestion=BigQueryInsertJobOperator(
        task_id="run_tags_ingestion",
        configuration={
            "load":{
                "sourceUris": [URI],
            "destinationTable": {
                "projectId": project_name,
                "datasetId": dataset_name,
                "tableId": table_name
            },
                "schema": {
                "fields": [
                    {"name": "userId", "type": "INTEGER"},
                    {"name": "movieId", "type": "INTEGER"},
                    {"name": "tag", "type": "STRING"},
                    {"name": "timestamp", "type": "INTEGER"},
                ]
            },               

            "skipLeadingRows": 1,
            "sourceFormat": "CSV",
            "writeDisposition": "WRITE_TRUNCATE"  # Or "WRITE_TRUNCATE"
        }
        },
        location="US",
        gcp_conn_id=conn_id

        

    )
    run_tags_ingestion

ingest_tags_to_bq()