import dlt
from dlt.sources.filesystem import filesystem, read_csv

#movielens 1M

URL='../../data/'

def load_csv_to_big_query(bucket_url, file_glob,pipeline_name,dataset_name,table_name):

    filesystem_pipe = filesystem(bucket_url=bucket_url, file_glob=file_glob) | read_csv()

    filesystem_pipe.apply_hints(write_disposition="replace")


    pipeline = dlt.pipeline(
        pipeline_name=pipeline_name,
        destination='bigquery', # <--- to run pipeline in production
        dataset_name=dataset_name, 
        dev_mode=False)

    info = pipeline.run(filesystem_pipe.with_name(table_name))
    print(f"File {file_glob} ingested to {table_name} in {dataset_name}")

if __name__ == "__main__":
    load_csv_to_big_query(bucket_url=URL,file_glob="movies.csv",pipeline_name="movies_data",
                          dataset_name="movie_lens",table_name="movies")