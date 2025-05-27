from airflow.decorators import dag,task
from pendulum import datetime
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
#we want to trigger it manually
#we dont want to rerun all past non-triggered dag runs
@dag(
    start_date=datetime(2025,5,25),
    schedule=None, 
    catchup=False, 
    tags=['retail']
)
def retail():
    upload_csv_to_gcs= LocalFilesystemToGCSOperator(
        task_id='upload_csv_to_gcs',
        src='/usr/local/airflow/include/data/ratings.csv',
        dst='airflow/ratings.csv',
        bucket='terraform-basics-458014-movielens',
        gcp_conn_id='gcp',
        mime_type='text/csv'
    )




    

retail()