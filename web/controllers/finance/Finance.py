# _*_ coding:utf-8 _*_
__author__ = 'solin'
__date__ = '2019/9/22 16:24'
from flask import Blueprint,render_template

route_finance = Blueprint('finance_page',__name__)
@route_finance.route("/index")
def index():
    return render_template("finance/index.html")

@route_finance.route("/account")
def account():
    return render_template("finance/account.html")

@route_finance.route("/pay-info")
def pay_info():
    return render_template("finance/pay_info.html")

