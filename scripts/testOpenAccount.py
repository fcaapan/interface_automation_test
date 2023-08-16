import re

import requests
from bs4 import BeautifulSoup

from api.reg_login_api import RegLoginApi

from api.open_account import OpenAccountApi


class TestOpenAccount(object):
    def setup_class(self):
        pass

    def setup(self):
        ses = requests.Session()
        self.obj_login = RegLoginApi(ses)
        self.obj_account = OpenAccountApi(ses)

    def test_realname(self):
        self.obj_login.user_login("18779095386", "qqq123")
        req = self.obj_account.realname("潘昌法", "360721199803074816")
        assert 200 == req.status_code

    def test01_account(self):
        self.obj_login.user_login("18779095386", "qqq123")
        req = self.obj_account.open_account()
        assert 200 == req.status_code

    def test02_thrid_account(self):
        self.obj_login.user_login("18779095386", "qqq123")
        req = self.obj_account.open_account()
        # print(req.json())
        data = BeautifulSoup(req.json().get("description").get("form"))
        # print(data)
        url = data.form.get("action")
        # print(url)
        inputs = data.find_all("input")
        form_dict = {}
        for input in inputs:
            form_dict[input.get("name")] = input.get("value")
        print(url,form_dict)
        req = self.obj_account.thrid_open_account(url, form_dict)
        # print(req)
        print("code",req.status_code)
        print(req.text)
        # partern="(action=')(.*?)('><input)"
        # url = re.findall(partern,str(req.json()))
        # print(f"url={url}")
        # partern="(name=')(.*?)(' type='hidden' value=')(.*?)('/>)"
        # values = re.findall(partern,str(req.json()))
        # print(values)
