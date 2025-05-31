{{ config(materialized='table') }}

select 
    zip_code, 
    city, 
    state_id, 
    state_name,
    county_name
from {{ ref('us_zip_codes') }}