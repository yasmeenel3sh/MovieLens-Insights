{{ config(materialized='view') }}

with base as (
    select
        movie_id,
        split(genres, '|') as genre_array
    from {{ ref('stg_movies') }}
),

unnested as (
    select
        movie_id,
        genre
    from base,
    unnest(genre_array) as genre
)

select * from unnested