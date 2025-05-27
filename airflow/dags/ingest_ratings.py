from airflow.decorators import dag,task
from pendulum import datetime
from include.code.data_ingestion.ratings_ingestion import load_csv_to_big_query

file_bucket_url="gs://terraform-basics-458014-movielens/movie_lens/ratings.csv"
project_name="terraform-basics-458014"
dataset_name="movie_lens"
table_name="raw_ratings"

@dag(
    start_date=datetime(2025,5,25),
    schedule=None, 
    catchup=False, 
    tags=['ingest_ratings']
)

def ingest_ratings_to_bq():
    
    @task
    def run_ratings_ingestion():
        load_csv_to_big_query(file_bucket_url=file_bucket_url,
                          project_name=project_name,
                          dataset_name=dataset_name,
                          table_name=table_name)
    run_ratings_ingestion()

ingest_ratings_to_bq()