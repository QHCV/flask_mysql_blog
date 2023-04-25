# 解决循环引用的问题
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
#数据库操作
db=SQLAlchemy()

mail = Mail()