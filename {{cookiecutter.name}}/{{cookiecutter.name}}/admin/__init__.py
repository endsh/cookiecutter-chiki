# coding: utf-8
from chiki import init_uploads
from chiki.admin import ModelView
from ..base import admin, db, login

sync_models = []


def init(app):
    """ 初始化后台管理 """

    # admin.add_view(StaticFileAdmin(app.config['STATIC_FOLDER'], '/static/', name='文件'))

    admin.init_app(app)
    db.init_app(app)
    init_uploads(app)

    login.init_app(app)

    @login.user_loader
    def load_user(id):
        try:
            # return User.objects(id=id).get()
            pass
        except DoesNotExist:
            pass