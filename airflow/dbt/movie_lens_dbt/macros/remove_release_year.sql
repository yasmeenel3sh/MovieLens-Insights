{#
    This macro return the title without the release year
#}

{% macro remove_release_year(title_column) %}
 regexp_replace({{ title_column }}, r'\s\(\d{4}\)$', '')
{% endmacro %}