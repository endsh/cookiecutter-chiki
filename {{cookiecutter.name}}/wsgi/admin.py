# coding: utf-8

try:
    from {{ cookiecutter.name }} import create_admin
    app = create_admin()
except Exception, e:
    from chiki import start_error    
    from {{ cookiecutter.name }}.config import AdminConfig
    start_error(config=AdminConfig)
