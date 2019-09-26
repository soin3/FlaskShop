# _*_ coding:utf-8 _*_
__author__ = 'solin'
__date__ = '2019/9/22 10:44'
import sys
from application import app, manager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Server
import www

manager.add_command("runserver",
                    Server(host="127.0.0.1", port=app.config["SERVER_PORT"], use_debugger=True, use_reloader=True))

# 添加迁移脚本的命令到manager中
manager.add_command('db', MigrateCommand)


def main():
    app.logger.info("*******服务已重启*******")
    manager.run()


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        import traceback

        traceback.print_exc()
