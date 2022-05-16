from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def config_extensions(app):
    db.init_app(app)
