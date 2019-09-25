# _*_ coding:utf-8 _*_
__author__ = 'solin'
__date__ = '2019/9/22 10:14'
'''
基础配置
'''

SERVER_PORT = 8000
DEBUG = False
SQLALCHEMY_ECHO = False
AUTH_COOKIE_NAME = "solin_shop"

IGNORE_URL = [
    "^/user/login"
]

IGNORE_LOGIN_URL = [
    "^/static",
    "^/favicon.ico"
]
