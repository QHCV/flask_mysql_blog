# Flask+mysql简单问答网站（实现公网可访问）

python版本3.8，提前安装好Mysql数据库

1.安装python包

```
pip install -r requirements.txt
```

2.修改配置文件config.py

- Mysql数据库用户名和密码
- 用于发送验证码的邮箱配置

​		在设置->账户下开启服务，获取授权码

![image-20230425173307729](../../../AppData/Roaming/Typora/typora-user-images/image-20230425173307729.png)

3.初始化数据库

```python
#只需要执行一次
flask db init 
# 将orm模型生成迁移脚本
flask db migrate
#将迁移脚本映射到数据库中
flask db upgrade
```

4.启动项目

```python
#开启Debug模式
set FLASK_ENV=development
#开启flask
flask run
```

5.使用ngrok实现公网访问

注册账号并登录：[ngrok - Online in One Line](https://ngrok.com/)

按照官网提示操作即可,最重要的是获取Authtoken

![image-20230425170538827](https://cdn.jsdelivr.net/gh/QHCV/picture-obs/2023.04/image-20230425170538827.png)

如果是Windows上操作，可直接点击ngrok.exe,然后在命令行中输入

```
ngrok config add-authtoken 【authtoken官网登录就可获取】
#flask端口号为5000
ngrok http 5000
```

![image-20230425170459445](https://cdn.jsdelivr.net/gh/QHCV/picture-obs/2023.04/image-20230425170459445.png)

实现效果：

登录和注册界面

![image-20230425170735322](https://cdn.jsdelivr.net/gh/QHCV/picture-obs/2023.04/image-20230425170735322.png)

![image-20230425171011666](https://cdn.jsdelivr.net/gh/QHCV/picture-obs/2023.04/image-20230425171011666.png)

参考自B站视频：https://www.bilibili.com/video/BV17r4y1y7jJ?p=1&vd_source=5fa56c12fe9967e30fac13bd17123f89