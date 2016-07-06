# coding: utf-8
from chiki.base import db
from chiki.contrib.users import UserManager
from chiki.api import api, wapi
from chiki.oauth import WeRoBot
{% if cookiecutter.has_api -%}
from flask import Blueprint
{%- endif %}

from {{ cookiecutter.name }}.config import BaseConfig

um = UserManager()
{%- if cookiecutter.has_api %}
page = Blueprint('page', __name__)
{%- endif %}
robot = WeRoBot()
