# coding: utf-8
from chiki.mongoengine import MongoEngine
from chiki.contrib.users import UserManager
from chiki.api import api, wapi
{% if cookiecutter.has_api -%}
from flask import Blueprint
{%- endif %}

from {{ cookiecutter.name }}.config import BaseConfig

db = MongoEngine()
um = UserManager()
{%- if cookiecutter.has_api %}
page = Blueprint('page', __name__)
{%- endif %}
