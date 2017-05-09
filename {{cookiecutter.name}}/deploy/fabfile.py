# coding: utf-8
import os
from chiki import import_file
from chiki.deploy import *
from fabric.api import env

password = ''
env.update(dict(
    user='dev',
    password=password,
    user_password=password,
    sudo_password='',
    project='{{ cookiecutter.name }}',
    path='/home/dev/data/{{ cookiecutter.name }}',
    src='/home/dev/src',
    dist='/home/dev/dist',
    repo='git@gitlab.com:xiaoku/{{ cookiecutter.name }}.git',
    shell="/bin/bash -l -i -c",
    apps=['admin'
    {%- if cookiecutter.has_api %}, 'api'{% endif %}
    {%- if cookiecutter.has_web %}, 'web'{% endif %}],
))

root = os.path.dirname(__file__)
puppets = [x for x in os.listdir(root) if os.path.isfile('%s/env.py' % x)]
modules = dict((x, import_file('%s/env.py' % x)) for x in puppets)

env.stage = 'all'
env.envs = dict((x, y.env) for x, y in modules.iteritems())
