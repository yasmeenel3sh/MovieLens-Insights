from airflow.decorators import dag
from pendulum import datetime
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
#we want to trigger it manually
#we dont want to rerun all past non-triggered dag runs
source='/usr/local/airflow/include/data/ratings.csv'
destination='airflow/ratings.csv'
bucket='terraform-basics-458014-movielens'
conn_id='gcp',

@dag(
    start_date=datetime(2025,5,25),
    schedule=None, 
    catchup=False, 
    tags=['ratings_upload']
)
def upload_ratings_to_gcs():
    upload_rating_to_gcs= LocalFilesystemToGCSOperator(
        task_id='upload_ratings_to_gcs',
        src=source,
        dst=destination,
        bucket=bucket,
        gcp_conn_id=conn_id,
        mime_type='text/csv'
    )

upload_ratings_to_gcs()