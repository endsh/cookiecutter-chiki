# coding: utf-8
from {{ cookiecutter.name }}.base import db, um

db.abstract(um.models.User)


@um.add_model
class User(um.models.User):
    """ 用户模型 """

    meta = dict(indexes=['phone', 'nickname', 'ip', '-logined', '-registered'])

    def __unicode__(self):
        return str(self.id)
