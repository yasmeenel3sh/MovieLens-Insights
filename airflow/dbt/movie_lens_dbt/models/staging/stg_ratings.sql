{{
    config(
        materialized= 'view' 
    )
}}

with ratings_data as (
    select *
    from {{source('staging', 'ratings_external')}}
) 
select 
   --identifiers
   {{dbt.safe_cast("userId",api.Column.translate_type("integer"))}} as user_id,
   {{dbt.safe_cast("movieId", api.Column.translate_type("integer"))}} as movie_id,
   {{dbt.safe_cast("rating",api.Column.translate_type("integer"))}} as rating,
   TIMESTAMP_SECONDS({{ dbt.safe_cast('timestamp', api.Column.translate_type('integer')) }}) as rating_timestamp
from ratings_data

-- dbt build --select <model_name> --vars '{'is_test_run': 'false'}'
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}