from flask import Flask
from app.views import config_blueprint
from .extensions import config_extensions
from .config import Config


def create_app(configName = "default"):
    app = Flask(__name__)
    # 加载配置文件内容
    ConfigDic = Config()
    app.config.from_object(ConfigDic)
    # 注册蓝本
    config_blueprint(app)
    # 初始化扩展库
    config_extensions(app)
    return app
