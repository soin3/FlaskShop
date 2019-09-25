# _*_ coding:utf-8 _*_
__author__ = 'solin'
__date__ = '2019/9/22 10:49'
import os, logging
import pymysql
from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy


'''
封装flask的局部变量，包括app，数据库等
'''


class Application(Flask):
    def __init__(self, import_name, template_folder=None, root_path=None):
        super(Application, self).__init__(import_name, template_folder=template_folder, root_path=root_path,
                                          static_folder=None)
        self.config.from_pyfile('config/base_setting.py')
        '''
        区分不同环境配置文件进行配置
        使用方法：
        linux命令行运行export ops_config=local或者export ops_config=production
        windows 命令行运行set ops_config=local或者set ops_config=production
        '''
        if "ops_config" in os.environ:
            self.config.from_pyfile('config/%s_setting.py' % os.environ['ops_config'])
        # self.config.from_pyfile('config/local_setting.py')
        # self.config.from_pyfile('config/production_setting.py')
        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__, template_folder=os.getcwd() + "/web/templates/", root_path=os.getcwd())

"""
日志系统配置
"""
handler = logging.FileHandler('app.log', encoding='UTF-8')
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
handler.setFormatter(logging_format)
app.logger.addHandler(handler)

"""
数据库配置：
使用Migrate绑定app和db
"""
manager = Manager(app)
migrate = Migrate(app, db)
pymysql.install_as_MySQLdb()

'''
函数模板
'''
from common.libs.UrlManager import UrlManager

app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')


