from airflow.decorators import dag
from pendulum import datetime
from airflow.operators.bash import BashOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from airflow.models import Variable
GCP_CONN_ID = Variable.get("GCP_CONN_ID", default_var="gcp")


CREATE_EXTERNAL_MOVIES_TABLE_SQL="""CREATE OR REPLACE EXTERNAL TABLE `terraform-basics-458014.movie_lens.movies_external`
OPTIONS (
  format = 'CSV',
  uris = ['gs://terraform-basics-458014-movielens/airflow/movies.csv'],
  skip_leading_rows = 1
);"""

@dag(
    start_date=datetime(2025,5,25),
    schedule=None,
    catchup=False,
    tags=['external_movies']
)
def create_external_movies_table_in_bq():
    create_external_movies_table = BigQueryInsertJobOperator(
    task_id="create_external_movies_table",
    configuration={
        "query": {
            "query": CREATE_EXTERNAL_MOVIES_TABLE_SQL,
            "useLegacySql": False,
        }
    },
    location="US",  
    gcp_conn_id=GCP_CONN_ID,
)
    
create_external_movies_table_in_bq()