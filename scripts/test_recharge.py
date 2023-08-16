import random

import requests
from bs4 import BeautifulSoup

from api.recharge_api import RechargeApi
from api.reg_login_api import RegLoginApi
class TestRecharge(object):
    def setup(self):
        ses =requests.Session()
        self.obj =RechargeApi(ses)
        self.obj_login =RegLoginApi(ses)
    def test_recharge_verify(self):
        self.obj_login.user_login("18779095386", "qqq123")
        r=random.randint(100000,999999)
        req =self.obj.recharge_verify(r)
        print(req)

    def test_recharge(self):
        self.obj_login.user_login("18779095386", "qqq123")
        self.obj.recharge_verify(9999999)
        req=self.obj.recharge("10000","8888")
        json_data =req.json()
        assert 200 == req.status_code

    def test_third_recharge(self):
        self.obj_login.user_login("18779095386", "qqq123")
        self.obj.recharge_verify(9999999)
        req = self.obj.recharge("10000", "8888")
        data = BeautifulSoup(req.json().get("description").get("form"))
        # print(data)
        url = data.form.get("action")
        # print(url)
        inputs = data.find_all("input")
        form_dict = {}
        for input in inputs:
            form_dict[input.get("name")] = input.get("value")
        print(url,form_dict)
        req = self.obj.third_recharge(url,form_dict)
        print(req.text)
        assert 200 == req.status_code
        assert 'OK' in req.text
