# coding: utf-8
import os

ROOT = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
LOG_FOLDER = os.path.join(ROOT, 'logs')
STATIC_FOLDER = os.path.join(ROOT, 'media/web/dist')

LOGGING = {
    'SMTP': {
        'HOST': 'smtp.mxhichina.com',
        'TOADDRS': ['438985635@qq.com'],
        'SUBJECT': u'{{ cookiecutter.name }} web 出错了 :-(',
        'USER': '{{ cookiecutter.log_email_user }}',
        'PASSWORD': '{{ cookiecutter.log_email_password }}',
    },
    'FILE': {
        'PATH': os.path.join(LOG_FOLDER, 'web.log'),
        'MAX_BYTES': 1024 * 1024 * 10,
        'BACKUP_COUNT': 5,
    }
}
