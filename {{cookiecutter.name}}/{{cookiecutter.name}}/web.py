# coding: utf-8
from chiki import MediaManager, init_uploads
from .base import db, login

media = MediaManager(
    css=['css/web.min.css'],
    cssx=[
        'libs/bootstrap/css/bootstrap.css', 
        'dist/css/web.css'
    ],
    js=['js/web.min.js'],
    jsx=[
        'libs/jquery-1.11.1.js', 
        'libs/jquery.form.js', 
        'libs/bootstrap/js/bootstrap.js',
        'dist/js/web.js'
    ],
)


def init_routes(app):
    pass


def init(app):
    db.init_app(app)
    media.init_app(app)
    login.init_app(app)
    login.login_view = '.login'

    @login.user_loader
    def load_user(id):
        try:
            # return User.objects(id=id).get()
            pass
        except DoesNotExist:
            pass

    init_uploads(app)
    init_routes(app)