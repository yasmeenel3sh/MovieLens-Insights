{{ config(materialized='view') }}

with users_data as (
    select *
    from {{ref('stg_users')}}
),
with zip_code_data as (
    select *
    from {{ref(us_zip_codes)}}
)
select 
    u.user_id,
    u.gender,
    u.age,
    u.occupation,
    u.zip_code,
    z.city,
    z.state_id,
    z.state_name,
    z.county_name
from users_data u
left join zip_code_data z
    on u.zip_code = z.zip_code