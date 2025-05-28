from airflow.decorators import dag,task
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from pendulum import datetime

URI="gs://terraform-basics-458014-movielens/airflow/movies.csv"

project_name="terraform-basics-458014"
dataset_name="movie_lens"
table_name="raw_movies"
conn_id="gcp"

@dag(
    start_date=datetime(2025,5,25),
    schedule=None,
    catchup=False,
    tags=['ingest_movies']
)

def ingest_movies_to_bq():
    run_movies_ingestion=BigQueryInsertJobOperator(
        task_id="run_movies_ingestion",
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
                    {"name": "movieId", "type": "INTEGER"},
                    {"name": "title", "type": "STRING"},
                    {"name": "genres", "type": "STRING"},
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

ingest_movies_to_bq()