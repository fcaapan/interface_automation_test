import os,sys

import requests

sys.path.append(os.getcwd())
import logging
from base.request_base import Requests
from config import BASE_URL
class RegLoginApi():
    def __init__(self):
        #继承Request,用于在子类的构造函数中调用父类的构造函数
        super().__init__(BASE_URL)
    # 获取图片验证码接口
    def get_img_verify_code(self):
        '''
        获取图片验证码接口
        '''
        url =  "/verifycode"
        resp = self.get(url=url)
        return resp

    # 获取短信验证码接口
    def get_phone_verify_code(self, phone, img_code_v, type_v="reg"):
        ''''''
        url = "/sendSms"
        from_dict_message = {"phone": phone, "imgVerifyCode": img_code_v, "type": type_v}
        resp = self.post(url=url, data=from_dict_message)
        logging.info("获取短信验证码接口的响应体数据：{}".format(resp.json()))
        return resp

    # 注册接口
    def user_register(self, form_dict):
        url = "/reg"
        resp = self.post(url=url,data=form_dict)
        print("获取注册接口的响应体数据：{}".format(resp.json()))
        return  resp


    # 登录接口
    def user_login(self, username, pwd):
        url = "/login"
        form_dict_login = {"username":username,"password":pwd}
        resp = self.post(url=url, json=form_dict_login)
        print(resp)
        logging.info("获取登录接口的响应体数据：{}".format(resp.json()))
        return resp

if __name__ == '__main__':
    # obj =RegLoginApi()
    # obj.user_login("1877449095386","123456")
    url ="http://www.bilibili.com/video/BV1LV411t7wg"
    url ="https://space.bilibili.com/1629347259"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    req = requests.get(url=url,headers=headers)
    print(req.text)