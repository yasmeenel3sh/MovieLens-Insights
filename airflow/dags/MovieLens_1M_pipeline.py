from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from pendulum import datetime

with DAG(
    dag_id="MovieLens_1M_pipeline",
    start_date=datetime(2025, 5, 25),
    schedule=None,
    catchup=False,
) as dag:

    trigger_dag_upload_movies = TriggerDagRunOperator(
        task_id="trigger_upload_movies",
        trigger_dag_id="upload_movies"
    )

    trigger_dag_upload_ratings = TriggerDagRunOperator(
        task_id="trigger_upload_ratings",
        trigger_dag_id="upload_ratings"
    )

    trigger_dag_upload_users = TriggerDagRunOperator(
        task_id="trigger_upload_users",
        trigger_dag_id="upload_users"
    )

    trigger_dag_ext_movies = TriggerDagRunOperator(
        task_id="trigger_create_ext_movies_table",
        trigger_dag_id="create_external_movies_table_in_bq"
    )

    trigger_dag_ext_ratings = TriggerDagRunOperator(
        task_id="trigger_create_ext_ratings_table",
        trigger_dag_id="create_external_ratings_table_in_bq"
    )

    trigger_dag_ext_users = TriggerDagRunOperator(
        task_id="trigger_create_ext_users_table",
        trigger_dag_id="create_external_users_table_in_bq"
    )

    trigger_dag_dbt_run = TriggerDagRunOperator(
        task_id="trigger_dbt_run",
        trigger_dag_id="dbt_run"
    )

    trigger_dag_upload_movies >> trigger_dag_ext_movies
    trigger_dag_upload_ratings >> trigger_dag_ext_ratings
    trigger_dag_upload_users >> trigger_dag_ext_users

    [trigger_dag_ext_movies, trigger_dag_ext_ratings,trigger_dag_ext_users] >> trigger_dag_dbt_run