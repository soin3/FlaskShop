# _*_ coding:utf-8 _*_
__author__ = 'solin'
__date__ = '2019/9/22 10:48'
from application import app
from web.controllers.index import route_index
from web.controllers.user.User import route_user
from web.controllers.account.Account import route_account
from web.controllers.finance.Finance import route_finance
from web.controllers.food.Food import route_food
from web.controllers.member.Member import route_member
from web.controllers.stat.Stat import route_stat
from web.controllers.static import route_static

"""
拦截器
"""
from web.interceptors.AuthInterceptor import *


'''
HTTP模块相关初始化
进行蓝图功能的统一加载，所有url配置都在此
'''
app.register_blueprint(route_index, url_prefix="/")  # 管理后台入口
app.register_blueprint(route_user, url_prefix="/user")  # 管理后台用户信息相关
app.register_blueprint(route_account, url_prefix="/account")  # 管理后台账号相关
app.register_blueprint(route_finance, url_prefix="/finance")  # 管理后台财务相关
app.register_blueprint(route_food, url_prefix="/food")  # 管理后台美餐管理相关
app.register_blueprint(route_member, url_prefix="/member")  # 管理后台会员列表相关
app.register_blueprint(route_stat, url_prefix="/stat")  # 管理后台统计相关

app.register_blueprint(route_static, url_prefix="/static")  #静态文件

