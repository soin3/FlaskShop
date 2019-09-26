# _*_ coding:utf-8 _*_
__author__ = 'solin'
__date__ = '2019/9/22 14:53'
from flask import Blueprint,render_template,g
from application import app


route_index = Blueprint('index_page',__name__)

@route_index.route("/")
def index():
    user_info = g.user_info
    app.logger.info("当前登录用户:%s"%user_info.nickname)
    return render_template("index/index.html",user_info=user_info)
