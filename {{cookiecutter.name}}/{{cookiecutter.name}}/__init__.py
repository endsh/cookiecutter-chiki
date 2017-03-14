# coding: utf-8
from chiki import init_admin
{%- if cookiecutter.has_api %}, init_api{% endif %}
{%- if cookiecutter.has_web %}, init_web{% endif %}
from {{ cookiecutter.name }} import admin
{%- if cookiecutter.has_api %}, api{% endif %}
{%- if cookiecutter.has_web %}, web{% endif %}
from {{ cookiecutter.name }}.config import AdminConfig
{%- if cookiecutter.has_api %}, APIConfig{% endif %}
{%- if cookiecutter.has_web %}, WebConfig{% endif %}


def create_admin(pyfile=None):
    return init_admin(admin.init, AdminConfig, pyfile=pyfile,
                      template_folder=AdminConfig.TEMPLATE_FOLDER)
{%- if cookiecutter.has_api %}


def create_api(pyfile=None):
    return init_api(api.init, APIConfig, pyfile=pyfile,
                    template_folder=APIConfig.TEMPLATE_FOLDER)
{%- endif %}
{%- if cookiecutter.has_web %}


def create_web(pyfile=None):
    return init_web(web.init, WebConfig, pyfile=pyfile,
                    template_folder=WebConfig.TEMPLATE_FOLDER)
{%- endif %}
