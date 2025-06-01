{{ config(
    materialized='view'
) }}

with ratings_agg as (
    select
        movie_id,
        title,
        release_year,
        count(*) as rating_count,
        avg(rating) as avg_rating
    from {{ ref('fact_ratings') }}
    group by movie_id, title, release_year
),

filtered as (
    select *
    from ratings_agg
    where rating_count >= 50
),

ranked as (
    select
        *,
        rank() over (order by avg_rating desc, rating_count desc) as rating_rank
    from filtered
)

select *
from ranked
order by rating_rank


{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}