import pytest
import requests
from api.reg_login_api import RegLoginApi
from common.sql_exe import clear_user_info
from common.read_data import read_json
import random
class TestRegLogin(object):
    # 实例化session对象
    ses =requests.Session()
    # 实例化session对象
    obj =RegLoginApi(ses)
    def setup_class(self):
        clear_user_info()
    data =read_json('reg_login_data',"img_verify_code")
    # 获取图片验证码测试用例
    @pytest.mark.parametrize("r,exp_status_code",data)
    def test01_img_verify_code(self,r,exp_status_code):
        req =self.obj.get_img_verify_code(r)
        assert exp_status_code == req.status_code


    data1 =read_json('reg_login_data',"phone_verify_code")
    @pytest.mark.parametrize("phone,imgVerifyCode,exp_status,description", data1)
    def test01_phone_verify_code(self, phone, imgVerifyCode,exp_status,description):
        self.obj.get_img_verify_code("123456")
        req = self.obj.get_phone_verify_code(phone,imgVerifyCode)
        json_data =req.json()
        assert 200 == req.status_code
        assert json_data.get("status") == exp_status
        assert description in json_data.get("description")


    data3 =read_json('reg_login_data',"user_register")
    @pytest.mark.parametrize("form_dict,exp_status,description", data3)
    def test01_user_register(self,form_dict, exp_status, description):
        self.obj.get_img_verify_code("123456")
        mobile =form_dict.get("phone")
        self.obj.get_phone_verify_code(mobile, "8888")
        req=self.obj.user_register(form_dict)
        json_data = req.json()
        assert 200 == req.status_code
        assert json_data.get("status") == exp_status
        assert description in json_data.get("description")

    data4 =read_json('reg_login_data',"user_login")
    @pytest.mark.parametrize("mobile,password,exp_status,description", data4)
    def test01_user_login(self,mobile, password,exp_status, description):
        self.obj.get_img_verify_code("123456")
        self.obj.get_phone_verify_code(mobile, "8888")
        req =self.obj.user_login(mobile,password)
        json_data = req.json()
        assert 200 == req.status_code
        assert json_data.get("status") == exp_status
        assert description in json_data.get("description")


