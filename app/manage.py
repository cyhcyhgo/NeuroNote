import os
from flask import Flask
# from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from __init__ import create_app

config_name = os.environ.get('FLASK_CONFIG') or 'default'
app = create_app(config_name)


if __name__ == '__main__':
    app.run()