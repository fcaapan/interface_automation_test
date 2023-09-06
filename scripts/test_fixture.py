import pytest
import requests

from api.reg_login_api import RegLoginApi

# @pytest.fixture(scope=xxx,params=xxx,autouse=xxx)　
#
# 　　　　fiixture装饰器可以传单三个参数
#
# 　　　　　　1：scope参数：初始化清除定义级别
#
# 　　　　　  2：params:参数
#
# 　　　　　　3：autouse：是否自动化执行　

@pytest.fixture(scope="class",autouse=True)
def setup():
    # 执行前置操作，例如设置测试环境或准备测试数据
    print("执行前置操作")
    # 可以返回一些数据，供测试用例使用
    yield "前置操作返回的数据"
    # 可以在yield之后执行一些后置操作，例如清理测试环境
    print("执行后置操作")

def test_example(setup):
    # 测试用例函数可以接收前置操作返回的数据
    print("执行测试用例")
    print("前置操作返回的数据：", setup)
    # 执行测试断言等操作








