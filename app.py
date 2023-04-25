from flask import Flask, session, g, redirect
import config
from exts import db , mail
from models import UserModel
# 导入蓝图
from blueprints.qa import bp as qa_bp
from blueprints.auth import bp as auth_bp
from flask_migrate import Migrate

# blueprint：用来做模块化的
# 电影、读书、音乐、xxx

# flask db init：只需要执行一次
# flask db migrate：将orm模型生成迁移脚本
# flask db upgrade：将迁移脚本映射到数据库中



app = Flask(__name__)
# 绑定配置文件
app.config.from_object(config)
#初始化数据库
db.init_app(app)
mail.init_app(app)

migrate = Migrate(app,db)
#注册蓝图
app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)

#befor_request /
#hook钩子函数g
@app.before_request
def my_before_request():
    user_id =session.get("user_id")
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g,"user",user)
    else:
        setattr(g,"user",None)

# 上下文处理器
@app.context_processor
def my_context_processor():
    return {"user":g.user}




# set FLASK_ENV=development
if __name__ == '__main__':
    app.run(debug=True)
