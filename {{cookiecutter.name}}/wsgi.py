# coding: utf-8
from {{ cookiecutter.name }} import create_admin
{%- if cookiecutter.has_api %}, create_api{% endif %}
{%- if cookiecutter.has_web %}, create_web{% endif %}

admin = create_admin()
{%- if cookiecutter.has_api %}
api = create_api()
{% endif %}
{%- if cookiecutter.has_web %}
web = create_web()
{% endif %}