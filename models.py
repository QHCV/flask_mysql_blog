from datetime import datetime
from exts import db

class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key =True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(300),nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)


class EmailCaptchaModel(db.Model):
    __tablename__ = "email_captcha"
    id = db.Column(db.Integer,primary_key =True,autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    email_captcha = db.Column(db.String(100), nullable=False)
    used = db.Column(db.Boolean,default=False)

class QuestionModel(db.Model):
    __tablename__ = "question"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    #设置外键
    author_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    author=db.relationship(UserModel,backref="questions")

class AnswerModel(db.Model):
    __tablename__ = "answer"
    id  = db.Column(db.Integer,primary_key=True,autoincrement=True)
    content = db.Column(db.Text,nullable=False)
    create_time=db.Column(db.DateTime, default=datetime.now)

    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    question = db.relationship(QuestionModel,backref=db.backref("answers",order_by=create_time.desc()))
    author = db.relationship(UserModel,backref="answers")
