{{
    config(
        materialized= 'view' 
    )
}}

with movies_data as (
    select *
    from {{source('staging', 'movies_external')}}
)
select 
   --identifiers
   -- identifiers
   {{ dbt.safe_cast("movieId", api.Column.translate_type("integer")) }} as movie_id,
   {{ dbt.safe_cast(get_release_year("title"), api.Column.translate_type("integer"))}} as release_year ,  
   {{ dbt.safe_cast(remove_release_year("title"), "STRING") }} as title,
   {{ dbt.safe_cast("genres","STRING") }} as genres

from movies_data

-- dbt build --select <model_name> --vars '{'is_test_run': 'false'}'
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}