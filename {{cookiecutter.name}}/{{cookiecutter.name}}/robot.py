# coding: utf-8
from chiki.contrib.common import Item
from datetime import datetime
from flask import current_app
from werobot.reply import TransferCustomerServiceReply
from {{ cookiecutter.name }}.base import robot, um


def subscribe(message):
    """ 关注 """
    return '欢迎关注'


@robot.text
def on_text(message):
    if message.content == u'客服':
        return '正在链接客服...'
    return TransferCustomerServiceReply(message=message)


@robot.subscribe
def on_subscribe(message):
    return subscribe(message)


@robot.unsubscribe
def on_unsubscribe(message):
    user = um.models.User.get_wechat(mp_openid=message.source)
    if user:
        user.wechat_user.unsubscribe()


@robot.scan
def scan(message):
    return subscribe(message)


def create_menu():
    buttons = [
        dict(name='首页', type='view', url='http://'),
        dict(name='别点我', sub_button=[
            dict(name='测试', type='view', url='http://'),
        ]),
        dict(name='个人中心', sub_button=[
            dict(name='个人中心', type='view', url='http://'),
        ]),
    ]
    current_app.wxclient.create_menu(dict(button=buttons))
