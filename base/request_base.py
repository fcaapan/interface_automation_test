import requests
import sys
import os
import json
sys.path.append(os.getcwd())

from common.logginger import logger


class Requests():
    '''
    封装重写requests方法
    '''
    def __init__(self, BASE_URL):
        # BASEURL为基准地址
        self.base_url = BASE_URL
        # 通过session达到保持cookie的目的
        self.session = requests.session()
        self.headers = {
            "X-CSRFToken": re.search(r'csrftoken=([^;]+)', cookie).group(1),
            "Cookie": cookie
        }

    def get(self, url, **kwargs):
        '''
        发送GET请求
        :param url: 请求地址
        :param kwargs: 其他参数
        :return: 返回响应对象
        '''
        headers = self.headers.copy()
        return self.request(url, "GET", headers=headers,**kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        '''
        发送POST请求
        :param url: 请求地址
        :param data: 表单数据
        :param json: json数据
        :param kwargs: 其他参数
        :return: 返回响应对象
        '''
        headers=self.headers.copy()
        headers["Content-Length"] = "<calculated when request is sent>"
        headers["Content-Type"] = "application/json;charset=UTF-8"
        return self.request(url, "POST", data, json, headers=headers,**kwargs)

    def put(self, url, data=None, **kwargs):
        '''
        发送PUT请求
        :param url: 请求地址
        :param data: 表单数据
        :param kwargs: 其他参数
        :return: 返回响应对象
        '''
        headers = self.headers.copy()
        headers["Content-Length"] = "<calculated when request is sent>"
        headers["Content-Type"] = "application/json;charset=UTF-8"
        return self.request(url, "PUT", data,headers=headers, **kwargs)

    def delete(self, url, **kwargs):
        '''
        发送DELETE请求
        :param url: 请求地址
        :param kwargs: 其他参数
        :return: 返回响应对象
        '''
        headers=self.headers
        return self.request(url, "DELETE", headers=headers,**kwargs)
    
    def request(self, url, method, data=None, json=None, **kwargs):
        '''
        封装requests方法
        :param url:url地址
        :param method:请求方法如get、post、put、delete等
        :param data:表单数据
        :param json:json数据
        :param kwargs:其他参数
        :return: 返回响应对象
        '''
        url = self.base_url + url
        headers = kwargs.get("headers")
        params = kwargs.get("params")
        files = kwargs.get("files")
        cookies = kwargs.get("cookies")

        # 将请求信息打印到log
        self.requests_log(url, method, data, json, params, headers, files, cookies)
        try:
            # 处理请求
            if method == "GET":
                res = self.session.get(url, **kwargs)
            elif method == "POST":
                res = self.session.post(url, data, json, **kwargs)
            elif method == "PUT":
                if json:
                    # session中PUT中没有提供直接使用json参数的方法，因此需要用data来传入
                    # 将一个JSON对象 json 转换为一个字符串
                    data = json.dumps(json)
                res = self.session.put(url, data, **kwargs)
            elif method == "DELETE":
                res = self.session.delete(url, **kwargs)
            else:
                raise ValueError("Invalid request method: {}".format(method))
            # 将响应信息打印到log
            self.response_log(res)
            return res
        except requests.exceptions.RequestException as e:
            logger.error("RequestException occurred: {}".format(e))
        except Exception as e:
            logger.error("An error occurred: {}".format(e))

    def requests_log(self, url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None):
        '''
        打印请求信息到日志
        :param url: 请求地址
        :param method: 请求方法
        :param data: 表单数据
        :param json: json数据
        :param params: 请求参数
        :param headers: 请求头
        :param files: 上传文件
        :param cookies: 请求cookies
        :return: None
        '''
        logger.info("接口请求地址 ==>> {}".format(url))
        logger.info("接口请求方式 ==>> {}".format(method))
        logger.info("接口请求头 ==>> {}".format(headers))
        logger.info("接口请求 params 参数 ==>> {}".format(params))
        logger.info("接口请求体 data 参数 ==>> {}".format(data))
        logger.info("接口请求体 json 参数 ==>> {}".format(json))
        logger.info("接口上传附件 files 参数 ==>> {}".format(files))
        logger.info("接口 cookies 参数 ==>> {}".format(cookies))

    def response_log(self, response):
        '''
        打印响应信息到日志
        :param response: 响应对象
        :return: None
        '''
        logger.info("接口响应状态码 ==>> {}".format(response.status_code))
        logger.info("接口响应头 ==>> {}".format(response.headers))
        logger.info("接口响应体 ==>> {}".format(response.text))
        try:
            response_json = response.json()
            response_json_str = json.dumps(response_json, ensure_ascii=False, indent=4)
            logger.info("接口响应体 ==>> {}".format(response_json_str))
        except ValueError:
            logger.info("接口响应体无法解析为JSON格式")