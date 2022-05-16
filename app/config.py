import os
from datetime import timedelta
import configparser

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY') or '654321'
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

    # 初始化Flask实例，对当前环境的配置初始化
    @staticmethod
    def init_app(app):
        pass

    def __init__(self):
        cf = configparser.ConfigParser()
        cf.read(basedir + r'\config.ini', encoding='utf-8')
        is_mysql = cf.getboolean("mysql", "is_mysql")
        if is_mysql:
            mysql_host = cf.get("mysql", "host")
            mysql_port = cf.get("mysql", "port")
            mysql_db_name = cf.get("mysql", "db_name")
            mysql_user = cf.get("mysql", "user")
            mysql_password = cf.get("mysql", "password")
            self.SQLALCHEMY_DATABASE_URI = \
                'mysql+pymysql://{a}:{b}@{c}:{d}/{e}?charset=utf8'.format(a=mysql_user, b=mysql_password,
                                                             c=mysql_host, d=mysql_port, e=mysql_db_name)