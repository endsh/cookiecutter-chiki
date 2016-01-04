# coding: utf-8
from chiki import init_uploads
from chiki.admin import ModelView, IndexView, get_static_admin
from {{ cookiecutter.name }}.base import db
from {{ cookiecutter.name }}.config import BaseConfig, WebConfig

sync_models = []


def init(app):
    """ 初始化后台管理 """

    admin = Admin(
        name=BaseConfig.SITE_NAME,
        index_view=IndexView(BaseConfig.SITE_NAME, menu_icon_value='diamond'),
        base_template='base.html',
    )

    admin.category_icon_classes = {
        u'运营': 'fa fa-hdd-o',
        u'日志': 'fa fa-database',
    }

    WebStaticAdmin = get_static_admin('WebStaticAdmin')
    admin.add_view(WebStaticAdmin(WebConfig.RELEASE_STATIC_FOLDER,
        'http://{{ cookiecutter.web_host }}/static/', name='文件', menu_icon_value='folder'))

    admin.init_app(app)
    db.init_app(app)
    init_uploads(app)
