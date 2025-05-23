import dlt
from dlt.sources.filesystem import filesystem, read_csv

#movielens 1M

URL='../../data/'

filesystem_pipe = filesystem(bucket_url=URL, file_glob="ratings.csv") | read_csv()

filesystem_pipe.apply_hints(write_disposition="replace")


pipeline = dlt.pipeline(
    pipeline_name='ratings_data',
    destination='bigquery', # <--- to run pipeline in production
    dataset_name="movie_lens", 
    dev_mode=False)

info = pipeline.run(filesystem_pipe.with_name("ratings"))
print(info)