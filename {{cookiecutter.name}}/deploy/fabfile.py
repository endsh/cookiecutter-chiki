# coding: utf-8
from fabric.api import cd, env, local, run, sudo
from fabric.api import execute, hosts, lcd, put
from fabric.contrib.files import exists, append

env.user = 'simple@chiki.org'
env.password = ''
ROOT = 'root@chiki.org'
PROJECT_NAME = '{{ cookiecutter.name }}'
SOURCE_FOLDER = '/home/%s/%s' % ('{{ cookiecutter.name }}', PROJECT_NAME)
REPO_URL = 'git@gitlab.com:tinysh/{{ cookiecutter.name }}.git'


def all():
    execute(init)
    execute(deploy)
    execute(nginx)


@hosts(ROOT)
def init():
    build()
    user('congra')


def build():
    sudo('apt-get update')
    sudo('apt-get install -y vim software-properties-common')
    sudo('apt-get install -y python-setuptools')
    sudo('easy_install pip supervisor')
    sudo('apt-get install -y python-virtualenv virtualenvwrapper')
    sudo('apt-get install -y python-dev subversion curl')
    sudo('apt-get install -y libmysqlclient-dev git gcc g++ unzip')
    sudo('apt-get install -y nginx mongodb')


def user(name):
    if not exists('/home/%s' % name):
        sudo('adduser %s' % name)
    run('mkdir -p /home/%s/.ssh' % name)
    put('files/id_rsa', '/home/%s/.ssh' % name)
    run('chmod 600 /home/%s/.ssh/id_rsa' % name)
    run('chown -R %s:%s /home/%s' % (name, name, name))


@hosts(env.user)
def deploy(extends=False):
    clone_code()
    mkvir(extends=extends)
    mkenv()


@hosts(env.user)
def update():
    clone_code()


def clone_code(source_folder=SOURCE_FOLDER):
    if exists(source_folder + '/.git'):
        run('cd %s && git stash && git pull' % source_folder)
    else:
        run('git clone %s %s' % (REPO_URL, source_folder))


def clone2setup(name, git):
    if not exists(name):
        run('git clone %s %s' % (git, name))
    else:
        run('cd %s && git stash && git pull' % name)
    with cd(name):
        run('~/.virtualenvs/%s/bin/python setup.py install' % name)


def mkvir(name=PROJECT_NAME, source_folder=SOURCE_FOLDER, extends=False):
    run('~/.virtualenvs/%s/bin/pip install -r %s/deploy_requestments.txt' % (name, source_folder))

    if extends:
        mkextends()


def mkextends():
    run('mkdir -p ~/git')
    gits = {
       'chiki': "https://https://github.com/endsh/chiki.git",
       'flask-admin': "https://github.com/flask-admin/flask-admin.git",
    }
    with cd('~/git'):
        for name, git in gits.iteritems():
            clone2setup(name, git)


def mkenv(source_folder=SOURCE_FOLDER):
    put('files/.bash_profile', '~/.bash_profile')
    append('~/.bashrc' , 'source ~/.bash_profile')
    for dirname in ['etc', 'run', 'logs']:
        run('mkdir -p %s/%s' % (source_folder, dirname))

    etc = '%s/%s' % (source_folder, 'etc')
    put('etc/admin.cfg', etc)
    put('etc/uwsgi-admin.ini', etc)
    {%- if cookiecutter.has_api %}
    put('etc/api.cfg', etc)
    put('etc/uwsgi-api.ini', etc)
    {%- endif %}
    {%- if cookiecutter.has_web %}
    put('etc/web.cfg', etc)
    put('etc/uwsgi-web.ini', etc)
    {%- endif %}


def sync():
    commit()
    execute(update)


def commit():   
    local('git add --all ..')
    local('git commit -m "auto commit"')
    local('git push -u origin master')


@hosts(env.user)
def pip():
    run('pip install -r %s/deploy_requirements.txt' % SOURCE_FOLDER)


def spip():
    sync()
    execute(pip)


@hosts(ROOT)
def nginx():
    nginx_config()
    nginx_reload()


def nginx_config():
    put('nginx/congra.nginx.conf', '/etc/nginx/sites-enabled')


def nginx_reload():
    run('service nginx reload')


@hosts(env.user)
def uwsgi_start():
    run('~/.virtualenvs/%s/bin/uwsgi --ini %s/etc/uwsgi-admin.ini' % (PROJECT_NAME, SOURCE_FOLDER))
    {%- if cookiecutter.has_api %}
    run('~/.virtualenvs/%s/bin/uwsgi --ini %s/etc/uwsgi-api.ini' % (PROJECT_NAME, SOURCE_FOLDER))
    {%- endif %}
    {%- if cookiecutter.has_web %}
    run('~/.virtualenvs/%s/bin/uwsgi --ini %s/etc/uwsgi-web.ini' % (PROJECT_NAME, SOURCE_FOLDER))
    {%- endif %}


@hosts(env.user)
def uwsgi_stop():
    run('~/.virtualenvs/%s/bin/uwsgi --stop %s/run/admin.pid' % (PROJECT_NAME, SOURCE_FOLDER))
    {%- if cookiecutter.has_api %}
    run('~/.virtualenvs/%s/bin/uwsgi --stop %s/run/api.pid' % (PROJECT_NAME, SOURCE_FOLDER))
    {%- endif %}
    {%- if cookiecutter.has_web %}
    run('~/.virtualenvs/%s/bin/uwsgi --stop %s/run/web.pid' % (PROJECT_NAME, SOURCE_FOLDER))
    {%- endif %}


@hosts(env.user)
def uwsgi_reload():
    run('~/.virtualenvs/%s/bin/uwsgi --reload %s/run/admin.pid' % (PROJECT_NAME, SOURCE_FOLDER))
    {%- if cookiecutter.has_api %}
    run('~/.virtualenvs/%s/bin/uwsgi --reload %s/run/api.pid' % (PROJECT_NAME, SOURCE_FOLDER))
    {%- endif %}
    {%- if cookiecutter.has_web %}
    run('~/.virtualenvs/%s/bin/uwsgi --reload %s/run/web.pid' % SOURCE_FOLDER)
    {%- endif %}
