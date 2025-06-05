from cosmos.config import ProfileConfig, ProjectConfig
from pathlib import Path

#The target_name you pass to ProfileConfig overrides whatever is written in the target: field of profiles.yml.

DBT_CONFIG = ProfileConfig(
    profile_name='movie_lens_dbt_pipeline_airflow',
    # target_name='prod',
    target_name='dev',
    profiles_yml_filepath=Path('/usr/local/airflow/dbt/movie_lens_dbt/profiles.yml')
)

DBT_PROJECT_CONFIG = ProjectConfig(
    dbt_project_path='/usr/local/airflow/dbt/movie_lens_dbt/'
)