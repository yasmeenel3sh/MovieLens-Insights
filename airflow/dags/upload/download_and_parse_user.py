from airflow.decorators import dag, task
from datetime import datetime
import pandas as pd
import requests, io
from zipfile import ZipFile
import os
#doesn't mount to local files
@dag(start_date=datetime(2025, 5, 25), schedule=None, catchup=False, tags=['download_and_extract_users'])
def movielens_dag():
    @task
    def download_and_parse():
        extract_dir = '/tmp/ml-1m'
        os.makedirs(extract_dir, exist_ok=True)

        url = 'https://files.grouplens.org/datasets/movielens/ml-1m.zip'
        response = requests.get(url)
        with ZipFile(io.BytesIO(response.content), 'r') as zip_ref:
            zip_ref.extractall(extract_dir)

        df = pd.read_csv(f'{extract_dir}/ml-1m/users.dat', sep='::', engine='python',
                         names=['userId', 'gender', 'age','occupation','zipCode'], encoding='ISO-8859-1')
        output_path = f'{extract_dir}/users.csv'
        df.to_csv(output_path, index=False)
        return output_path

    download_and_parse()

movielens_dag()
