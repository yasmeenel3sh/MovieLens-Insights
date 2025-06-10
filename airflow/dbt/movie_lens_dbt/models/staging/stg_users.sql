{{
    config(
        materialized= 'view' 
    )
}}

with users_data as (
    select *
    from {{source('staging', 'users_external')}}
)
select 
   --identifiers
   -- identifiers
   {{ dbt.safe_cast("UserID", api.Column.translate_type("integer")) }} as user_id,
   {{ dbt.safe_cast("Gender", "STRING") }} as gender,
   {{ dbt.safe_cast("Age","STRING") }} as age,
   {{ dbt.safe_cast("Occupation","STRING") }} as occupation,
   {{ dbt.safe_cast("Zip_code",api.Column.translate_type("integer")) }} as zip_code
--    where zip_code is not null

from users_data

-- dbt build --select <model_name> --vars '{'is_test_run': 'false'}'
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}