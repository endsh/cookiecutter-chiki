# coding: utf-8
from chiki import register_web, MediaManager, init_uploads
from {{ cookiecutter.name }}.base import db, um, wapi, WebConfig

media = MediaManager(
    css=['css/web.min.css'],
    cssx=[
        'bower_components/weui/dist/style/weui.css',
        'node_modules/jquery-weui/dist/css/jquery-weui.css',
        'bower_components/bxslider-4/dist/jquery.bxslider.min.css',
        'dist/css/web.css',
    ],
    js=['js/web.min.js'],
    jsx=[
        'bower_components/jquery/dist/jquery.js',
        'bower_components/jquery-form/jquery.form.js',
        'bower_components/jquery-tmpl/jquery.tmpl.js',
        'bower_components/bxslider-4/dist/jquery.bxslider.min.js',
        'node_modules/jquery-weui/dist/js/jquery-weui.js',
        'node_modules/jquery-weui/dist/js/city-picker.js',
        'node_modules/jquery-weui/dist/js/swiper.js',
        'bower_components/jquery_lazyload/jquery.lazyload.js',
        'bower_components/fastclick/lib/fastclick.js',
        'dist/js/web.js',
    ]
)


def init_routes(app):
    pass


def init_um(app):
    um.init_app(app)
    um.init_wapis(wapi)
    um.init_web()


@register_web(config=WebConfig)
def init(app):
    db.init_app(app)
    media.init_app(app)
    init_um(app)
    init_routes(app)
    init_uploads(app)
    wapi.init_app(app)
