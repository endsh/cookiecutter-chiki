# coding: utf-8
from chiki import init_uploads
from chiki.admin import Admin, ModelView, IndexView, get_static_admin
from chiki.contrib.common import Item, StatLog, TraceLog
from chiki.contrib.common import ItemView, StatLogView, TraceLogView
from {{ cookiecutter.name }}.base import db
from {{ cookiecutter.name }}.config import BaseConfig, WebConfig

sync_models = []


def init(app):
    """ 初始化后台管理 """

    admin = Admin(
        name=BaseConfig.SITE_NAME,
        index_view=IndexView('仪表盘', menu_icon_value='diamond'),
        base_template='base.html',
    )

    admin.category_icon_classes = {
        u'运营': 'fa fa-hdd-o',
        u'日志': 'fa fa-database',
    }

    # 日志
    admin.add_view(ItemView(Item,           name='系统选项', category='日志'))
    admin.add_view(StatLogView(StatLog,     name='统计日志', category='日志'))
    admin.add_view(TraceLogView(TraceLog,   name='跟踪日志', category='日志'))

    WebStaticAdmin = get_static_admin('WebStaticAdmin')
    admin.add_view(WebStaticAdmin(WebConfig.RELEASE_STATIC_FOLDER,
        'http://{{ cookiecutter.web_host }}/static/', name='文件', menu_icon_value='folder'))

    admin.init_app(app)
    db.init_app(app)
    init_uploads(app)
