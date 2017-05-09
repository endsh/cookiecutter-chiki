# coding: utf-8
import os
import shutil

api_files = [
    '{{ cookiecutter.name }}/api',
    '{{ cookiecutter.name }}/wsgi/api.py',
    'media/api',
    'templates/api',
]
web_files = [
    '{{ cookiecutter.name }}/web',
    '{{ cookiecutter.name }}/wsgi/web.py',
    'media/web',
    'templates/web',
]


def delete(name):
    if os.path.isfile(name):
        os.remove(name)
    elif os.path.isdir(name):
        shutil.rmtree(name)


def main():
    {% if not cookiecutter.has_api %}
    for api in api_files:
        delete(api)
    {% endif %}

    {% if not cookiecutter.has_web %}
    for web in web_files:
        delete(web)
    {% endif %}

    os.system("mkdir -p deploy/files && echo \"deploy/files/id_rsa\" | ssh-keygen -t rsa -C \"438985635@qq.com\"")


if __name__ == '__main__':
    main()