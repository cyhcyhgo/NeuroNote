from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class User_info(FlaskForm):
    name = StringField('', validators=[DataRequired()],
                       render_kw={"type": "text", "placeholder": "用户名", 'maxlength': '20'})
    password = PasswordField('', validators=[DataRequired()],
                             render_kw={"placeholder": "密码", 'maxlength': '10', 'minlength': '6'})
    isAdministrator = BooleanField('', render_kw={"id": "check"})
    submit = SubmitField('登录', render_kw={"id": "but"})


class Manage_user_info(User_info):
    user_id = StringField('', validators=[DataRequired()], render_kw={"type": "text", })


class Register(FlaskForm):
    username = StringField('', validators=[DataRequired()],
                           render_kw={'type': 'text', 'class': 'input_wide', 'placeholder': '用户名', 'maxlength': '20'})
    password = PasswordField('', validators=[DataRequired()],
                             render_kw={'placeholder': '请输入密码', 'class': 'input_wide', 'maxlength': '10',
                                        'minlength': '6'})
    password2 = PasswordField('', validators=[DataRequired()],
                              render_kw={'placeholder': '请确认密码', 'class': 'input_wide', 'maxlength': '10',
                                         'minlength': '6'})
    captcha = StringField('', validators=[DataRequired()],
                          render_kw={'type': 'text', 'id': "captcha", 'placeholder': '请输入验证码', 'maxlength': '4',
                                     'autocomplete': "off"})
    submit = SubmitField('注册', render_kw={'id': 'but'})
