# _*_ coding:utf-8 _*_
__author__ = 'solin'
__date__ = '2019/9/22 15:06'
import json
from application import app
from flask import Blueprint, render_template, request, jsonify, make_response,redirect
from common.libs.user.UserService import UserTool
from common.models import User

route_user = Blueprint('user_page', __name__)


@route_user.route("/login", methods={"GET", "POST"})
def login():
    ret = {"code": "-1", "msg": "", "data": {}}
    if request.method == "GET":
        return render_template("user/login.html")
    elif request.method == "POST":
        req = request.values
        app.logger.info("请求路径：%s，请求参数：%s" % (request.path, req))
        login_name = req["login_name"] if "login_name" in req else ""
        login_pwd = req["login_pwd"] if "login_pwd" in req else ""
        if login_name is None and len(login_name) < 1:
            ret["msg"] = "请输入正确的用户名和密码"
            app.logger.info("%s用户名输错" % login_name)
            return jsonify(ret)
        if login_pwd is None and len(login_pwd) < 1:
            ret["msg"] = "请输入正确的用户名和密码"
            app.logger.info("%s密码输错，输入为:%s" % (login_name, login_pwd))
            return jsonify(ret)

        try:
            user = User.UserInfo.query.filter_by(login_name=login_name).first()
            # app.logger.info(str(user))
        except Exception as e:
            app.logger.error(e)

        if user:
            lib_pwd = UserTool.makepwd(login_pwd, user.login_salt)
            if user.login_pwd == lib_pwd:
                ret["code"] = 200
                ret["msg"] = "登陆成功"
                app.logger.info("%s登陆成功" % login_name)
                response = make_response(json.dumps(ret))
                lib_cookie = UserTool.makecookie(user)
                app.logger.info("%s生成的cookie：%s" % (login_name, lib_cookie))
                response.set_cookie(app.config['AUTH_COOKIE_NAME'], '%s#%s' % (
                    lib_cookie, user.id), 60 * 60 * 24 * 120)  # cookie保存120天

                return response
            else:
                ret["msg"] = "请输入正确的用户名和密码"
                app.logger.info("%s密码输错，输入为:%s" % (login_name, login_pwd))
                return jsonify(ret)
        else:
            app.logger.info("%s账号不存在" % login_name)
            ret["msg"] = "请输入正确的用户名和密码"
            return jsonify(ret)


@route_user.route("/edit")
def edit():
    return render_template("user/edit.html")


@route_user.route("/reset_pwd")
def reset_pwd():
    return render_template("user/reset_pwd.html")

@route_user.route("/logout")
def logout():
    app.logger.info("退出登录")
    response = make_response(redirect("/user/login"))
    response.delete_cookie(app.config["AUTH_COOKIE_NAME"])
    return response