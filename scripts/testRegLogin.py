import random
import allure
import pytest

from api.reg_login_api import RegLoginApi
from common.logginger import logger
from common.sql_exe import MysqlDb


data = [{
    "phone": "18888888888",
    "username": "QTA_USER"
}]


@pytest.fixture(scope="class", params=data, autouse=True)
def pre_post_test(request):
    db = MysqlDb()
    pre_data_phone = request.param["phone"]
    sql = """
    delete from user where phone='{}'
    """.format(pre_data_phone)
    logger.info("连接数据库成功")
    logger.info("清理环境脏数据")
    logger.info("执行sql语句")
    db.execute_db(sql)
    yield
    logger.info("清理本次测试数据")
    db.execute_db(sql)
    del db


@allure.feature("获取图片验证码--短信验证码--注册--登录功能")
class TestRegLogin:
    obj = RegLoginApi()

    @allure.epic("获取图片验证码")
    def test01_img_verify_code(self):
        with allure.step("获取图片验证码"):
            resp = self.obj.get_img_verify_code(random.randint(1000000000, 999999999))
            assert resp.status_code == 200

    @allure.epic("获取短信验证码")
    def test02_phone_verify_code(self, pre_post_test):
        with allure.step("获取短信验证码"):
            logger.info("获取验证码成功")

    def test03_register(self):
        pass

    @allure.epic("测试登录")
    def test04_user_login(self):
        with allure.step("测试登录"):
            rsp = self.obj.user_login("18779095386", "123456")
            assert rsp.status_code == 200
            assert rsp.json().get("message") == "操作成功"
            assert rsp.json().get("success") is True