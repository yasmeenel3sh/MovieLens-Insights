{#
    This macro splits the release year from the title and return the year
#}

{% macro get_release_year(title_column) -%}
CAST(REGEXP_EXTRACT({{ title_column }}, r'\((\d{4})\)$') AS INT64)
{%- endmacro %}