{{ config(materialized='view') }}

with ratings as (
    select
        user_id,
        movie_id,
        rating,
        rating_timestamp as rating_timestamp
    from {{ ref('stg_ratings') }}
),

users as (
    select
        user_id,
        age,
        gender,
        occupation,
        zip_code,
        state_name
    from {{ ref('dim_users') }}
),

movies as (
    select
        movie_id,
        title,
        release_year
    from {{ ref('stg_movies') }}
),

time_dim as (
    select
        rating_timestamp,
        year,
        month
    from {{ ref('dim_time') }}
)

select
    r.user_id,
    u.age,
    u.gender,
    u.occupation,
    u.zip_code,
    u.state_name,

    r.movie_id,
    m.title,
    m.release_year,

    r.rating,
    r.rating_timestamp

    t.year,
    t.month

from ratings r
left join users u on r.user_id = u.user_id
left join movies m on r.movie_id = m.movie_id
left join time_dim t on r.rating_timestamp = t.rating_timestamp

{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}