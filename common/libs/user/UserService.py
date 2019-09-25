# _*_ coding:utf-8 _*_
__author__ = 'solin'
__date__ = '2019/9/24 17:28'
import hashlib,base64

"""
用户模块公用工具类
"""
class UserTool():
    @staticmethod
    def makepwd(login_pwd,login_salt):
        """
        生成加密密码
        """
        str = "%s-%s"%(login_pwd,login_salt)
        pwd_base64 = base64.b64encode(str.encode('utf-8'))
        m = hashlib.md5()
        m.update(pwd_base64)
        pwd = m.hexdigest()
        return pwd

    @staticmethod
    def makecookie(user=None):
        """
        生成加密cookie
        """
        str = "%s-%s-%s-%s"%(user.id,user.login_name,user.login_pwd,user.login_salt)
        cookie_base64 = base64.b64encode(str.encode('utf-8'))
        m = hashlib.md5()
        m.update(cookie_base64)
        cookie = m.hexdigest()
        return cookie



    # @staticmethod
    # def genePwd( pwd,salt):
    #     m = hashlib.md5()
    #     str = "%s-%s" % ( base64.encodebytes( pwd.encode("utf-8") ) , salt)
    #     print(str)
    #     m.update(str.encode("utf-8"))
    #     res= m.hexdigest()
    #     print(res)


if __name__ == "__main__":
    """
    测试样例：
    login_pwd：123456
    login_salt：cF3JfH5FJfQ8B2Ba

    """
    AA = UserTool.makepwd("123456","cF3JfH5FJfQ8B2Ba")
    print(AA)
    # UserTool.genePwd("123456","cF3JfH5FJfQ8B2Ba")
    #"816440c40b7a9d55ff9eb7b20760862c"






