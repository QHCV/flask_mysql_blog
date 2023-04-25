SECRET_KEY = "asdfasdfjasdfjasd;lf"

# 数据库的配置信息
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'zhijianxiaosuo'
USERNAME = 'root'
PASSWORD = 'XXXX'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI


# 邮箱配置，这里用QQ邮箱
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465

#用于发送邮件的邮箱，需要的邮箱中进行相关权限设置
MAIL_USERNAME = "XXX@qq.com"
MAIL_PASSWORD = "XXX"
MAIL_DEFAULT_SENDER = "XXX@qq.com"