import requests
from bs4 import BeautifulSoup

from common.sql_exe import init_tender_info
from api.invest import Invest
from api.reg_login_api import RegLoginApi

class TestTender(object):

    def setup_class(self):
        # 借款标测试数据初始化
        init_tender_info()

    def setup(self):
        # 创建session对象
        ses =requests.Session()

        # 调用投资模块类
        self.obj_invest = Invest(ses)

        # 调用登录模块类
        self.obj_login =RegLoginApi(ses)


    # 投资测试用例
    def test01_tender(self):
        # 用户登录
        self.obj_login.user_login("18779095386", "qqq123")

        # 投资
        req=self.obj_invest.invest("642","1000")
        json_data =req.json()
        assert 200 == req.status_code

    # 第三方投资测试用例
    def test02_third_tender(self):
        self.obj_login.user_login("18779095386", "qqq123")
        # 投资
        req = self.obj_invest.invest("642", "1000")
        data = BeautifulSoup(req.json().get("description").get("form"))
        # print(data)
        url = data.form.get("action")
        # print(url)
        inputs = data.find_all("input")
        form_dict = {}
        for input in inputs:
            form_dict[input.get("name")] = input.get("value")
        # print(url, form_dict)
        req = self.obj_invest.third_invest(url, form_dict)
        assert 200 == req.status_code
        assert 'OK' in req.text
