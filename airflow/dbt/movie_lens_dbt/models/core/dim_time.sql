{{ config(materialized='view') }}

with raw_timestamps as (
    select distinct rating_timestamp as ts
    from {{ ref('stg_ratings') }}
),

final as (
    select
        ts as full_datetime,
        extract(year from ts) as year,
        extract(month from ts) as month,
        extract(day from ts) as day,
        extract(dayofweek from ts) as day_of_week,
        format_date('%Y-%m', date(ts)) as year_month,
        format_date('%Y-%m-%d', date(ts)) as full_date
    from raw_timestamps
)

select * from final

{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}