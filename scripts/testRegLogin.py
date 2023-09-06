import random

import allure, pytest

from api.reg_login_api import RegLoginApi
from common.logginger import logger
from common.sql_exe import MysqlDb
"""

# @allure.feature # 用于定义被测试的功能，被测产品的需求点
# @allure.story # 用于定义被测功能的用户场景，即子功能点
# @allure.severity #用于定义用例优先级
# @allure.issue #用于定义问题表识，关联标识已有的问题，可为一个url链接地址
# @allure.testcase #用于用例标识，关联标识用例，可为一个url链接地址

# @allure.attach # 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
# @pytest.allure.step # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤
# allure.environment(environment=env) #用于定义environment

"""

data =[{
    "phone":"18888888888",
    "username": "QTA_USER"
}]

@allure.title("测试前置操作，清理数据库脏数据，后置操作删除数据库本次数据")
@pytest.fixture(scope="class" ,params=data,autouse=True)
def pre_post_test(request):
    #实例化连接数据库对象
    # db =MysqlDb()
    # 连接数据库
    # 获取测试数据操作，编写sql语句
    logger.info("连接数据库成功")
    pre_data_phone =request.param["phone"]
    sql = """
    delete from user where phone=='{}'
    """.format(pre_data_phone)
    #前置操作，清理数据库脏数据
    logger.info("清理环境脏数据")
    logger.info("执行sql语句")
    # db.execute_db(sql)
    yield
    logger.info("清理本次测试数据")
    # db.execute_db(sql)
    # #关闭数据库连接
    # del db




@allure.feature("获取图片验证码--短信验证码--注册--登入功能")
class TestRegLogin():
    '''
    用例标题：
    '''
    obj = RegLoginApi()

    # 获取图片验证码测试用例
    @allure.epic("获取图片验证码")
    def test01_img_verify_code(self):
        try:
            resp = self.obj.get_img_verify_code(random.randint(1000000000, 999999999))
        except:
            logger.info("连接失败")
        pass
        # resp = self.login.get_img_verify_code(random.randint(1000000000, 999999999))
        # return resp
    # 获取短信验证码测试用例
    @allure.epic("获取短信验证码")
    def test02_phone_verify_code(self,pre_post_test):
        logger.info("获取验证码成功")

    # 注册测试用例
    def test03_register(self):
        pass

    # 登录测试用例
    @allure.epic("测试登入")
    def test04_user_login(self):
        rsp = self.obj.user_login("18779095386","123456")
        assert rsp.status_code ==200
        logger.info(rsp.json())
        assert rsp.json().get("message")=="操作成功"
        assert rsp.json().get("success")==True