import wtforms
from wtforms.validators import Email, Length, EqualTo, InputRequired
from exts import db
from models import UserModel, EmailCaptchaModel


# 主要用来做表单验证的
# 注册验证
class RegisterForm(wtforms.Form):
    email= wtforms.StringField(validators=[Email(message="邮箱格式错误!")])
    captcha = wtforms.StringField(validators=[Length(max=4,min=4,message="验证码格式错误！")])
    username = wtforms.StringField(validators=[Length(max=20,min=2,message="用户名格式错误！")])
    password = wtforms.StringField(validators=[Length(max=20,min=4,message="密码格式错误！")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])
    # 验证邮箱是否已经被注册了
    def validate_email(self, filed):
        email = filed.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="该邮箱已经被注册了！")
    # 验证码是否正确
    def validate_captcha(self, filed):
        captcha = filed.data
        email = self.email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email,email_captcha=captcha).first()
        if not captcha_model:
            raise wtforms.ValidationError(message="该邮箱或验证码错误！")
        else:
            db.session.delete(captcha_model)
            db.session.commit()
# 登录验证
class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误!")])
    password = wtforms.StringField(validators=[Length(max=20, min=4, message="密码格式错误！")])

#问答提交验证
class QuestionForm(wtforms.Form):
    title= wtforms.StringField(validators=[Length(min=3,max=100,message="标题格式错误!")])
    content= wtforms.StringField(validators=[Length(min=1,message="内容过少!")])

#问答提交验证
class AnswerForm(wtforms.Form):
    content= wtforms.StringField(validators=[Length(min=3,message="格式错误!")])
    question_id= wtforms.IntegerField(validators=[InputRequired(message="必须传入问题ID!")])
