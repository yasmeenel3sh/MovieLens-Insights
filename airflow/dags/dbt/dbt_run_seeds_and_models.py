from airflow.decorators import dag
from pendulum import datetime
from airflow.operators.bash import BashOperator
from airflow.models import Variable
from cosmos.airflow.task_group import DbtTaskGroup
from dbt.movie_lens_dbt.cosmos_config import DBT_PROJECT_CONFIG, DBT_CONFIG
from cosmos.constants import LoadMode, TestBehavior
from cosmos.config import RenderConfig

###########################################################
# DAG configuration

GCP_CONN_ID = Variable.get("GCP_CONN_ID", default_var="gcp")

@dag(
    schedule=None,
    # schedule="@daily",
    start_date=datetime(2025, 5, 25),
    catchup=False,
    tags=["dbt_run"],
)
def dbt_run_seeds_and_models():
    transform= DbtTaskGroup(
        group_id= 'transform',
        project_config= DBT_PROJECT_CONFIG,
        profile_config= DBT_CONFIG,
        render_config= RenderConfig(
            load_method= LoadMode.DBT_LS,
            #select=['path:seeds','path:models'],
            test_behavior=TestBehavior.AFTER_ALL,

            dbt_executable_path= "/usr/local/airflow/dbt_venv/bin/dbt"
            
            )

    )

    # return
    #     transform = BashOperator(
    #     task_id="transform",
    #     bash_command="source /usr/local/airflow/dbt_venv/bin/activate && dbt run --select path:models",
    #     cwd="/usr/local/airflow/dbt/movie_lens_dbt"
    # )
    transform
dbt_run_seeds_and_models()