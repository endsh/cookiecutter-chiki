# coding: utf-8

try:
    from {{ cookiecutter.name }} import create_api
    app = create_api()
except Exception, e:
    from chiki import start_error    
    from {{ cookiecutter.name }}.config import APIConfig
    start_error(config=APIConfig)