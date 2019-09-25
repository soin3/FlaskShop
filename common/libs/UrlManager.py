# -*- coding: utf-8 -*-
'''
链接管理器
'''


class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod
    def buildStaticUrl(path):
        # ver = "%s"%("v1")
        path = "/static" + path
        return UrlManager.buildUrl(path)


