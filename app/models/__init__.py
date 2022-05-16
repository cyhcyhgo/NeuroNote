import openpyxl as op
import os

from .user import Users


def initial_database(database):
    database.create_all()
    p5 = Users(id=1, username='CYH', password='123456', isAdministrator=1)
    p6 = Users(id=2, username='GX', password='654321', isAdministrator=0)
    database.session.add(p5)
    database.session.add(p6)
    database.session.commit()