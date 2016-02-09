# coding: utf-8
import os


class BaseConfig(object):
    """ 基础配置 """

    # 目录, i18n
    ROOT_FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_FOLDER = os.path.join(ROOT_FOLDER, 'data')
    DOC_FOLDER = os.path.join(ROOT_FOLDER, 'docs')
    LOG_FOLDER = os.path.join(ROOT_FOLDER, 'logs')
    STATIC_FOLDER = os.path.join(ROOT_FOLDER, 'media')
    TEMPLATE_FOLDER = os.path.join(ROOT_FOLDER, 'templates')
    BABEL_DEFAULT_LOCALE = 'zh_CN'
    CHANGE_400_TO_200 = True

    # Secret Key
    SECRET_KEY = 'SECRET KEY'
    PASSWORD_SECRET = 'PASSWORD SECRET'
    WTF_CSRF_SECRET_KEY = 'WTF CSRF SECRET KEY'

    MONGODB_SETTINGS = dict(host='127.0.0.1', port=27017, db='{{ cookiecutter.name }}')

    UPLOADS = dict(
        type='local', 
        link='/uploads/%s', 
        path=os.path.join(DATA_FOLDER, 'uploads'),
    )

    # 版本，网站名称等
    VERSION = '{{ cookiecutter.version }}'
    SITE_NAME = u'{{ cookiecutter.site_name }}'


class AdminConfig(BaseConfig):
    """ 后台管理通用配置 """

    PORT = {{ cookiecutter.port | int }}
    ENVVAR = '{{ cookiecutter.name | upper }}_ADMIN'
    SESSION_COOKIE_NAME = '{{ cookiecutter.name }}.admin'
    STATIC_FOLDER = os.path.join(BaseConfig.STATIC_FOLDER, 'admin')
    RELEASE_STATIC_FOLDER = os.path.join(BaseConfig.STATIC_FOLDER, 'admin/dist')
    TEMPLATE_FOLDER = os.path.join(BaseConfig.TEMPLATE_FOLDER, 'admin')

    INDEX_REDIRECT = '/admin/'

    # 后台管理员帐号密码
    ADMIN_USERNAME = 'admin'
    ADMIN_PASSWORD = ''
{%- if cookiecutter.has_api %}


class APIConfig(BaseConfig):
    """ 接口通用配置 """

    PORT = {{ cookiecutter.port | int + 1 }}
    ENVVAR = '{{ cookiecutter.name | upper }}_API'
    SESSION_COOKIE_NAME = '{{ cookiecutter.name }}.api'
    STATIC_FOLDER = os.path.join(BaseConfig.STATIC_FOLDER, 'api')
    RELEASE_STATIC_FOLDER = os.path.join(BaseConfig.STATIC_FOLDER, 'api/dist')
    TEMPLATE_FOLDER = os.path.join(BaseConfig.TEMPLATE_FOLDER, 'api')
{%- endif %}
{%- if cookiecutter.has_web %}


class WebConfig(BaseConfig):
    """ 网站通用配置 """

    PORT = {{ cookiecutter.port | int + 2 }}
    ENVVAR = '{{ cookiecutter.name | upper }}_WEB'
    SESSION_COOKIE_NAME = '{{ cookiecutter.name }}'
    STATIC_FOLDER = os.path.join(BaseConfig.STATIC_FOLDER, 'web')
    RELEASE_STATIC_FOLDER = os.path.join(BaseConfig.STATIC_FOLDER, 'web/dist')
    TEMPLATE_FOLDER = os.path.join(BaseConfig.TEMPLATE_FOLDER, 'web')
{%- endif %}
