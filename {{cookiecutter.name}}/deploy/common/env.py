# coding: utf-8

env = dict(
    branch='{{ cookiecutter.name }}-common',
    roledefs=dict(
        db=['root@hostname'],
        front=['root@hostname'],
        main=['hostname'],
        web=[
            'hostname',
        ],
        puppet=[
        ],
    ),
)
