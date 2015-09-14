# coding: utf-8

try:
    from {{ cookiecutter.name }} import create_web
    app = create_web()
except Exception, e:
    from chiki import start_error    
    from {{ cookiecutter.name }}.config import WebConfig
    start_error(config=WebConfig)