# coding: utf-8
import re
import os
from setuptools import setup, find_packages


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()


file_text = read(fpath('{{ cookiecutter.name }}/__init__.py'))


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval


def get_data_files(*dirs):
    results = []
    for src_dir in dirs:
        for root, dirs, files in os.walk(src_dir):
            results.append((root, map(lambda f: root + "/" + f, files)))
    return results


setup(
    name='{{ cookiecutter.name }}',
    version=grep('__version__'),
    url='http://example.com/',
    author=grep('__author__'),
    author_email=grep('__email__'),
    description='Common libs of flask web develop',
    packages=find_packages(),
    include_package_data=True,
    data_files=get_data_files('templates'),
    zip_safe=False,
    platforms='any',
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.name }} = chiki.cli:main',
        ]
    },
)
