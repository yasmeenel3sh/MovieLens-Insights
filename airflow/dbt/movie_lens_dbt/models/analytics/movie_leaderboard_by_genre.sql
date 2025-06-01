with ranked_movies as (
    select
        r.movie_id,
        r.title,
        r.release_year,
        g.genre,
        r.rating_count,
        r.avg_rating,
        rank() over (
            partition by g.genre 
            order by r.avg_rating desc, r.rating_count desc
        ) as genre_rank
    from {{ ref('dim_movies_genres') }} as g
    join (
        select
            movie_id,
            title,
            release_year,
            count(*) as rating_count,
            avg(rating) as avg_rating
        from {{ ref('fact_ratings') }}
        group by movie_id, title, release_year
        having count(*) >= 50
    ) as r
    on g.movie_id = r.movie_id
)

select *
from ranked_movies
where genre_rank <= 10




{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}