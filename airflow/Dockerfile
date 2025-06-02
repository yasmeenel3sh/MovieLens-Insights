FROM astrocrpublic.azurecr.io/runtime:3.0-2

ENV VENV_PATH="/usr/local/airflow/dbt_venv"
ENV PATH="$VENV_PATH/bin:$PATH" 

# install dbt into a virtual environment
RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-bigquery && deactivate


# Store environment activation script inside Airflow home
RUN echo "source $VENV_PATH/bin/activate" > /usr/local/airflow/dbt_env.sh
RUN chmod +x /usr/local/airflow/dbt_env.sh
