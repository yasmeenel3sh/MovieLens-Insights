from airflow.decorators import dag
from pendulum import datetime
from airflow.operators.bash import BashOperator
from airflow.models import Variable

###########################################################
# DAG configuration

GCP_CONN_ID = Variable.get("GCP_CONN_ID", default_var="gcp")

@dag(
    schedule=None,
    # schedule="@daily",
    start_date=datetime(2025, 5, 25),
    catchup=False,
    tags=["dbt_test"],
)
def dbt_test():
    dbt_test_raw = BashOperator(
            task_id="dbt_test_raw",
            bash_command="source /usr/local/airflow/dbt_venv/bin/activate && dbt test --select source:*",
            cwd="/usr/local/airflow/dbt/movie_lens_dbt"
        )

dbt_test()