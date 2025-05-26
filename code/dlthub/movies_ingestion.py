from google.cloud import bigquery

def load_csv_to_big_query(file_bucket_url,project_name,dataset_name,table_name):

# Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the table to create.
    table_id = f"{project_name}.{dataset_name}.{table_name}"

    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("movieId", "INT64"),
            bigquery.SchemaField("title", "STRING"),
            bigquery.SchemaField("genres", "STRING")
        ],
        skip_leading_rows=1,
        # The source format defaults to CSV, so the line below is optional.
        source_format=bigquery.SourceFormat.CSV,
    )
    uri = file_bucket_url

    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  # Make an API request.

    load_job.result()  # Waits for the job to complete.

    destination_table = client.get_table(table_id)  # Make an API request.
    print("Loaded {} rows.".format(destination_table.num_rows))

if __name__ == "__main__":
    load_csv_to_big_query(file_bucket_url="gs://terraform-basics-458014-movielens/movie_lens/links.csv",
                          project_name="terraform-basics-458014",
                          dataset_name="movie_lens",
                          table_name="movies")