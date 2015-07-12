# coding: utf-8
from chiki.admin import IndexView
from chiki.mongoengine import MongoEngine
{% if cookiecutter.has_api -%}
from chiki.api import api
from flask import Blueprint
{%- endif %}
from flask.ext.admin import Admin
from flask.ext.login import LoginManager
from .config import BaseConfig

admin = Admin(
    name=BaseConfig.SITE_NAME,
    index_view=IndexView(),
    base_template='base.html', 
    template_mode='bootstrap3',
)
db = MongoEngine()
login = LoginManager()
{%- if cookiecutter.has_api %}
page = Blueprint('page', __name__)
{%- endif %}