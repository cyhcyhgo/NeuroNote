from app.views import verificationCode
from flask import render_template, session, Blueprint

from app.forms import User_info, Register
from app.models import Users
from app.extensions import db

import os

basedir = os.path.abspath(os.path.dirname(__file__))

user = Blueprint('user', __name__)


# 验证码
@user.route('/imgCode')
def imgCode():
    return verificationCode.imageCode().getImgCode()


@user.route('/login', methods=['GET', 'POST'])
def login():
    form = User_info()
    message = ''
    isAlert = 0
    isJump = 0
    isAdministrator = 0
    if form.validate_on_submit():
        username = form.data['name']
        password = form.data['password']
        User = Users.query.filter(Users.username == username).first()
        isAdministrator = int(form.data['isAdministrator'])
        if User:
            if User.password == password:
                if User.isAdministrator == 0 and isAdministrator:
                    message = '您不是管理员'
                    isAlert = 1
                else:
                    message = '欢迎回来，' + User.username
                    session['user'] = User.username
                    session['user_id'] = User.id
                    session.permanent = True  # 默认为 31 天
                    isAlert = 1
                    isJump = 1
            else:
                isAlert = 1
                message = '密码错误'
        else:
            isAlert = 1
            message = '用户名不存在'
    return render_template('user/login.html',
                           message=message,
                           form=form,
                           isJump=isJump,
                           isAlert=isAlert,
                           isAdministrator=isAdministrator)


@user.route('/reg', methods=['GET', 'POST'])
def reg():
    form = Register()
    message = ' '
    isAlert = 0
    isJump = 0
    if form.validate_on_submit():
        username = form.data['username']
        password = form.data['password']
        password2 = form.data['password2']
        captcha = form.data['captcha'].lower()
        User = Users.query.filter(Users.username == username).first()
        if captcha != session['imageCode'].lower():
            isAlert = 1
            message = '验证码错误'
        elif User:
            isAlert = 1
            message = '该用户已经存在'
        elif password != password2:
            isAlert = 1
            message = '两次密码输入不一致'
        elif len(password) < 6:
            isAlert = 1
            message = '密码长度至少6个字符'
        else:
            new_user = Users(username=username, password=password, isAdministrator=0)
            db.session.add(new_user)
            db.session.commit()
            isAlert = 1
            message = '注册成功！即将跳转至登录界面'
            isJump = 1
    return render_template('user/reg.html', message=message, form=form, isJump=isJump, isAlert=isAlert)
