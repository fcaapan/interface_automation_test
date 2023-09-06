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

import os,sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))
import allure
import pytest


from common.logginger import logger
from common.sql_exe import MysqlDb

@allure.title("测试前置操作，清理数据库脏数据，后置操作删除数据库本次数据")
@pytest.fixture()
def pre_post_test(request):
    #实例化连接数据库对象
    db =MysqlDb()
    # 获取测试数据操作，编写sql语句
    pre_data_phone =request.param
    sql = """
    delete from user where phone=='{}'
    """.format(pre_data_phone)
    #前置操作，清理数据库脏数据
    logger.info("清理环境脏数据")
    db.execute_db(sql)
    yield
    logger.info("清理本次测试数据")
    db.execute_db(sql)
    #关闭数据库连接
    del db


def test_001(pre_post_test,name):
    print(1)



