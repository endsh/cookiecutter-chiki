# coding: utf-8
from chiki.admin import formatter_ip
from chiki.contrib.users.admin import UserView as _UserView
from {{ cookiecutter.name }}.base import db, um

db.abstract(um.models.User)


@um.add_model
class User(um.models.User):
    """ 用户模型 """

    meta = dict(indexes=['phone', 'nickname', 'ip', '-logined', '-registered'])

    def __unicode__(self):
        return str(self.id)


class UserView(_UserView):
    column_formatters = dict(
        ip=formatter_ip(url='/admin/user/?flt1_7=%(ip)s', blank=False),
    )
