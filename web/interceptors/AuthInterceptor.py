# _*_ coding:utf-8 _*_
__author__ = 'solin'
__date__ = '2019/9/25 10:05'
import re
from flask import request, redirect,g

from application import app
from common.models import User
from common.libs.user import UserService
from common.libs.UrlManager import UrlManager


"""
用户登陆拦截器
"""


@app.before_request
def before_request():
    path = request.path
    chk = checklogin()
    """
    忽略配置文件里的地址
    """
    ignore_url = app.config["IGNORE_URL"]
    ignore_login_url = app.config["IGNORE_LOGIN_URL"]
    pattern = re.compile('%s'%"|".join(ignore_login_url))
    if pattern.match(path):
        return
    pattern = re.compile('%s'%"|".join(ignore_url))
    if pattern.match(path):
        return
    app.logger.info("登陆拦截器验证结果：%s"%chk)
    if chk:
        return
    else:
        app.logger.info("跳转至登录页")
        return redirect(UrlManager.buildUrl("/user/login"))


def checklogin():
    cookies = request.cookies
    auth_cookies = cookies[app.config["AUTH_COOKIE_NAME"]] if app.config["AUTH_COOKIE_NAME"] in cookies else None

    if auth_cookies is not None:
        auth_info = auth_cookies.split("#")
        if len(auth_info) != 2:
            return False
        user_id = auth_info[1]
        try:
            """
            通过#分割cookie值，获取出主键id，先查有无此用户
            """
            user = User.UserInfo.query.filter_by(id=user_id).first()
        except Exception as e:
            app.logger.error(e)
            return False
        if user is not None:
            """
            再判断cookie的一致性
            """
            user_cookie = UserService.UserTool.makecookie(user)
            app.logger.info("当前user_cookie:%s" % user_cookie)
            request_cookie = auth_info[0]
            app.logger.info("当前request_cookie:%s" % request_cookie)
            if user_cookie == request_cookie:
                app.logger.info("user_id[%s]的cookie验证通过" % user_id)
                g.user_info = user
                return True
            else:
                app.logger.info("user_id[%s]的cookie不一致，验证失败" % user_id)
                return False
        else:
            return False
    else:
        return False




