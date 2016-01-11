# coding: utf-8
from chiki import MediaManager, init_uploads
from {{ cookiecutter.name }}.base import db, login

media = MediaManager(
    css=['css/web.min.css'],
    cssx=[
        'libs/bootstrap/css/bootstrap.css',
        'dist/css/web.css'
    ],
    js=['js/web.min.js'],
    jsx=[
        'bower_components/jquery/dist/jquery.js',
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
        return User.objects(id=id).first()

    init_uploads(app)
    init_routes(app)
