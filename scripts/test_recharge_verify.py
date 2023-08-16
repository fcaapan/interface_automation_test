import pytest
import requests
from api.reg_login_api import RegLoginApi
from api.recharge_api import RechargeApi
from common.read_data import read_json


class Testrecharge_verify(object):
    def setup(self):
        ses =requests.Session()
        obj =RechargeApi(ses)
        obj_login=RegLoginApi(ses)
    # # data1 =read_json('reg_login_data',"")
    # @pytest.mark.parametrize()
    # def test01(self):
    #




