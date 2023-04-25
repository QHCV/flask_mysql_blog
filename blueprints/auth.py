import random
from flask import Blueprint, render_template, request, jsonify, redirect, url_for,session  # 返回JSON数据
from exts import mail ,db
from flask_mail import Message
import string
from models import EmailCaptchaModel, UserModel
from .forms import RegisterForm,LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

bp =Blueprint("auth",__name__,url_prefix="/auth")


@bp.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱不存在，请先注册！")
                return redirect(url_for("auth.login"))
            if check_password_hash(user.password,password):
                session["user_id"]=user.id
                return redirect("/")
            else:
                print("登录失败，请检查密码是否正确！")
                return redirect(url_for("auth.login"))

        else:
            print(form.errors)
            return redirect(url_for("auth.login"))

@bp.route("/register",methods=["GET","POST"])
def register():
    if request.method=="GET":
        return  render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email =form.email.data
            username = form.username.data
            password = form.password.data
            user=UserModel(email=email,username=username,password=generate_password_hash( password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return  redirect(url_for("auth.register"))



@bp.route("/captcha/email")
def get_email_captcha():
    email = request.args.get("email")
    source = string.digits*5
    captcha1 = random.sample(source,4)
    captchanum = "".join(captcha1)
    message = Message(subject="智建小硕登录验证码", recipients=[email], body="本次的验证码为："+captchanum+"，三分钟内有效。")
    mail.send(message)
    # print(captcha)
    #redis 缓存机制/断电存储  要学！
    #数据库存储验证码
    email_captcha = EmailCaptchaModel(email= email,email_captcha=captchanum)
    db.session.add(email_captcha)
    db.session.commit()
    return jsonify({"code":200,"message":"","data":None})

@bp.route("/logout")
def logout():
    session.clear()
    return  redirect("/") #回到首页