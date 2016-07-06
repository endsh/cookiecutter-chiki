# coding: utf-8
import inspect
from flask.ext.script import Manager, Server
from {{ cookiecutter.name }} import create_admin
{%- if cookiecutter.has_api %}, create_api{% endif %}
{%- if cookiecutter.has_web %}, create_web{% endif %}
from {{ cookiecutter.name }}.config import BaseConfig, AdminConfig
{%- if cookiecutter.has_api %}, APIConfig{% endif %}
{%- if cookiecutter.has_web %}, WebConfig{% endif %}

manager = Manager(create_admin)
manager.add_command('admin', Server(port=AdminConfig.PORT))


{% if cookiecutter.has_api -%}
@manager.command
def api(debug=False, reloader=False, host='0.0.0.0', port=APIConfig.PORT):
    """ Run the api server. """
    app = create_api()
    app.run(debug=debug, use_reloader=reloader, host=host, port=port)


{% endif -%}
{% if cookiecutter.has_web -%}
@manager.command
def web(debug=False, reloader=False, host='0.0.0.0', port=WebConfig.PORT):
    """ Run the web server. """
    app = create_web()
    app.run(debug=debug, use_reloader=reloader, host=host, port=port)


{% endif -%}
@manager.command
def test():
    """ Run the tests. """
    import pytest
    exit_code = pytest.main([BaseConfig.TEST_FOLDER])
    return exit_code


@manager.command
@manager.option('name')
def service(name, model='simple'):
    module = '{{ cookiecutter.name }}.services.%s' % name
    action = __import__(module)
    for sub in module.split('.')[1:]:
        action = getattr(action, sub)
    if inspect.getargspec(action.run)[0]:
        action.run(model)
    else:
        action.run()


@manager.command
def create_menu():
    """ create wechat menu """
    from {{ cookiecutter.name }}.robot import create_menu
    create_menu()


if __name__ == '__main__':
    manager.run()
