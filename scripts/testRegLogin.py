import requests

from api.reg_login_api import RegLoginApi
import random


class TestRegLogin(object):
    # 实例化session对象
    ses = requests.Session()
    # 实例化session对象
    login = RegLoginApi(ses)

    # 获取图片验证码测试用例
    def test01_img_verify_code(self):
        resp = self.login.get_img_verify_code(random.randint(1000000000, 999999999))
        resp
    # 获取短信验证码测试用例
    def test02_phone_verify_code(self):
        pass

    # 注册测试用例
    def test03_register(self):
        pass

    # 登录测试用例
    def test04_user_login(self):
        pass
