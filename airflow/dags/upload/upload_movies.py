from airflow.decorators import dag
from pendulum import datetime
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
#we want to trigger it manually
#we dont want to rerun all past non-triggered dag runs
source='/usr/local/airflow/include/data/movies.csv'
destination='airflow/movies.csv'
bucket='terraform-basics-458014-movielens'
conn_id='gcp'

@dag(
    start_date=datetime(2025,5,25),
    schedule=None, 
    catchup=False, 
    tags=['movies_upload']
)
def upload_movies():
    upload_movies_to_gcs= LocalFilesystemToGCSOperator(
        task_id='upload_movies_to_gcs',
        src=source,
        dst=destination,
        bucket=bucket,
        gcp_conn_id=conn_id,
        mime_type='text/csv'
    )

upload_movies()