# coding: utf-8
import os
from chiki import register_admin, init_uploads, statistics
from chiki.admin import Admin, AdminIndexView, get_static_admin
from {{ cookiecutter.name }}.base import db, cm, um, BaseConfig, AdminConfig

sync_models = []
WebStaticAdmin = get_static_admin('WebStaticAdmin')


@statistics()
class IndexView(AdminIndexView):
    """ 仪表盘 """

    tabs = [
        dict(endpoint='.index', title='用户统计', text='用户'),
    ]

    u = um.models.User
    datas = dict(
        index=[
            dict(title='新用户统计', suffix='人', series=[
                dict(name='新用户', key='user_new'),
            ]),
            dict(title='活跃用户统计', suffix='人', series=[
                dict(name='活跃用户', key='user_active'),
            ]),
        ],
    )


@register_admin(config=AdminConfig)
def init(app):
    """ 初始化后台管理 """
    admin = Admin(
        name=BaseConfig.SITE_NAME,
        index_view=IndexView('仪表盘', menu_icon_value='diamond'),
        base_template='base.html',
    )
    
    if os.path.isdir(app.config.get('RELEASE_STATIC_FOLDER')):
        admin.add_view(WebStaticAdmin(
            app.config.get('RELEASE_STATIC_FOLDER'),
            'http://www.simple.com/static/',
            name='文件', menu_icon_value='folder'))

    admin.init_app(app)
    db.init_app(app)
    um.init_app(app)
    init_uploads(app)

    with app.app_context():
        cm.init_admin(admin)
