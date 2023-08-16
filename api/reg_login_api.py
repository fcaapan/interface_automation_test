from config import BASE_HOST


class RegLoginApi:

    def __init__(self, ses):
        self.ses = ses

    # 获取图片验证码接口
    def get_img_verify_code(self, r):
        url = BASE_HOST + "/common/public/verifycode1/{}".format(r)
        resp = self.ses.get(url=url)
        print("获取图片验证码接口的响应状态码：{}".format(resp.status_code))
        return resp

    # 获取短信验证码接口
    def get_phone_verify_code(self, phone, img_code_v, type_v="reg"):
        url = BASE_HOST + "/member/public/sendSms"
        from_dict_dx = {"phone": phone, "imgVerifyCode": img_code_v, "type": type_v}
        resp = self.ses.post(url=url, data=from_dict_dx)
        print("获取短信验证码接口的响应体数据：{}".format(resp.json()))
        return resp

    # 注册接口
    def user_register(self, form_dict):
        url = BASE_HOST + "/member/public/reg"
        resp = self.ses.post(url=url,data=form_dict)
        print("获取注册接口的响应体数据：{}".format(resp.json()))
        return  resp


        # 登录接口

    def user_login(self, username, pwd):
        url = BASE_HOST + "/member/public/login"
        form_dict_login = {"keywords":username,"password":pwd}
        resp = self.ses.post(url=url, data=form_dict_login)
        print("获取登录接口的响应体数据：{}".format(resp.json()))
        return resp

