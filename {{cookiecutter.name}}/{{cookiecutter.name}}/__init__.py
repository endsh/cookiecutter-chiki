# coding: utf-8
from {{ cookiecutter.name }} import admin
{%- if cookiecutter.has_api %}, api{% endif %}
{%- if cookiecutter.has_web %}, web{% endif %}

__version__ = '1.0.0'
__author__ = 'User'
__email__ = 'user@qq.com'

