import requests,sys,os
import json as complexjson
sys.path.append(os.getcwd())

from common.logginger import logger


class Requests():
    '''
    封装重写requests方法
    '''
    def __init__(self, BASE_URL):
        #BASEURL为基准地址
        self.base_url = BASE_URL
        #通过session达到保持cookie的目的
        self.session = requests.session()

    def get(self, url, **kwargs):
        return self.request(url, "GET", **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request(url, "POST", data, json, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request(url, "PUT", data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "DELETE", **kwargs)

    
    def request(self, url, method, data=None, json=None,**kwargs):
        '''
        封装requests方法
        :param url:url地址
        :param method:请求方法如get、post、put、delete等
        :param data:表单数据
        :param json:json数据
        :param kwargs:其他参数
        :return:
        '''
        # 将基准地址与请求路径参数拼接
        url = self.base_url + url
        dict(**kwargs)
        # 将kwargs字典解包为关键字参数，并创建一个新的字典对象。
        # 这样做的目的是为了确保kwargs是一个字典对象，以便可以使用字典的方法。
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("files")
        cookies = dict(**kwargs).get("cookies")

        #将请求信息打印到log
        self.requests_log(url, method, data, json, params, headers, files, cookies)
        try:
            # 处理请求
            if method =="GET":
                res = self.session.get(url,**kwargs)
            if method == "POST":
                res = requests.post(url, data, json, **kwargs)
            if method == "PUT":
                if json:
                    # session中PUT中没有提供直接使用json参数的方法，因此需要用data来传入
                    #将一个JSON对象 json 转换为一个字符串
                    data = complexjson.dumps(json)
                res =self.session.put(url, data, **kwargs)
            if method == "DELETE":
                res= self.session.delete(url, **kwargs)
        except Exception as e:
            logger.error("请求错误：{}".format(e))
            raise e
        else:
            self.response_log(res)
            return res

    def requests_log(self, url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None):
        logger.info("接口请求地址 ==>> {}".format(url))
        logger.info("接口请求方式 ==>> {}".format(method))
        logger.info("接口请求头 ==>> {}".format(headers))
        logger.info("接口请求 params 参数 ==>> {}".format(params))
        logger.info("接口请求体 data 参数 ==>> {}".format(data))
        logger.info("接口请求体 json 参数 ==>> {}".format(json))
        logger.info("接口上传附件 files 参数 ==>> {}".format(files))
        logger.info("接口 cookies 参数 ==>> {}".format(cookies))

    def response_log(self,res):
        status_code=res.status_code
        try:
            res_json=res.json()
        except Exception as e:
            res_json="返回的不是json数据"
        text=res.text
        logger.info("接口返回的状态码是 ==>> {}".format(status_code))
        logger.info("返回的json数据 ==>> {}".format(res_json))
        logger.info("接口请求头 ==>> {}".format(text))
