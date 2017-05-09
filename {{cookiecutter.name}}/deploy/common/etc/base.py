# coding: utf-8
import os

ROOT = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

DATA_FOLDER = os.path.join(ROOT, 'data')
ETC_FOLDER = os.path.join(ROOT, 'etc')
LOG_FOLDER = os.path.join(ROOT, 'logs')
RELEASE_STATIC_FOLDER = os.path.join(ROOT, 'media/web/dist')
