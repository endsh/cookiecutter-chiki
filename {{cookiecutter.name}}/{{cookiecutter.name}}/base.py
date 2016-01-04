# coding: utf-8
from chiki.mongoengine import MongoEngine
{% if cookiecutter.has_api -%}
from chiki.api import api
from flask import Blueprint
{%- endif %}
from flask.ext.login import LoginManager
from {{ cookiecutter.name }}.config import BaseConfig

db = MongoEngine()
login = LoginManager()
{%- if cookiecutter.has_api %}
page = Blueprint('page', __name__)
{%- endif %}