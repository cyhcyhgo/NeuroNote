# 蓝本配置
#from .main import main
from .user import user
#from .note import note

DEFAULT_BLUEPRINT = (
    #(main, ''),
    (user, '/user'),
    #(note, '/note'),
)


# 注册蓝本
def config_blueprint(app):
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)