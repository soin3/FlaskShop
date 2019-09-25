# _*_ coding:utf-8 _*_
__author__ = 'solin'
__date__ = '2019/9/24 9:44'
from application import db


class UserInfo(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="用户主键")
    nickname = db.Column(db.String(50), nullable=False, comment="昵称")
    mobile = db.Column(db.String(11), nullable=False, unique=True, comment="手机号")
    email = db.Column(db.String(100), nullable=True, server_default="")
    sex = db.Column(db.Integer, nullable=False, comment='性别(1：男 2：女 0：没填写)')
    avatar = db.Column(db.String(50), nullable=False, comment="头像")
    login_name = db.Column(db.String(20), nullable=False, unique=True, comment="登录名")
    login_pwd = db.Column(db.String(32), nullable=False, comment="登陆密码")
    login_salt = db.Column(db.String(32), nullable=False, comment="加密盐")
    status = db.Column(db.Integer, nullable=False, comment='账号状态(1：已删除  0：正常)')
    update_time = db.Column(db.DateTime, nullable=False)
    insert_time = db.Column(db.DateTime, nullable=False)



