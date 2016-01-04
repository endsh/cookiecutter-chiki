# coding: utf-8
from chiki import MediaManager, init_uploads
from {{ cookiecutter.name }}.base import api, page, db, login

media = MediaManager(
    css=['css/api.min.css'],
    cssx=[
        'libs/bootstrap/css/bootstrap.css',
        'dist/css/api.css'
    ],
    js=['js/api.min.js'],
    jsx=[
        'libs/jquery-1.11.1.js',
        'libs/jquery.form.js',
        'libs/bootstrap/js/bootstrap.js',
        'dist/js/api.js'
    ],
)


def init_routes(app):
    app.register_blueprint(page)


def init(app):
    api.init_app(app)
    db.init_app(app)
    media.init_app(app)
    login.init_app(app)
    login.login_view = '.login'

    @login.user_loader
    def load_user(id):
        return User.objects(id=id).first()

    init_uploads(app)
    init_routes(app)
