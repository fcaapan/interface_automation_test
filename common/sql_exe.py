import pymysql

from common.logginger import logger
from config import *

# 获取config文件的数据库信息
DB_CONF = {
    "host": mysql_config["MYSQL_HOST"],
    "port": mysql_config["MYSQL_PORT"],
    "user": mysql_config["MYSQL_USER"],
    "password": mysql_config["MYSQL_PASSWD"],
    "db": mysql_config["MYSQL_DB"]
}
logger.info("数据库的配置信息 %s " % DB_CONF)

# 测试拆包
# def test(**kwargs):
#     a, b, c, d, e =kwargs
#     print(a,b,c,d,e)
# test(**DB_CONF)
# host port user password db

class MysqlDb():

    def __init__(self, db_conf=DB_CONF):
        # 通过字典拆包传递配置信息，建立数据库连接
        if not all(db_conf.values()):
            raise ValueError("database configuration ERROR")  # 抛出值错误异常，数据库配置不完整
        self.conn = pymysql.connect(**db_conf, autocommit=True)  # 建立数据库连接
        self.cur = self.conn.cursor()
        logger.info("数据库连接成功")

    def __del__(self):  # 对象资源被释放时触发，在对象即将被删除时的最后操作
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()
        logger.info("数据库连接关闭")

    def select_db(self, sql):
        """查询"""
        if not sql:
            raise ValueError("Empty SQL")  # 抛出值错误异常，SQL语句为空
        self.conn.ping(reconnect=True)  # 检查数据库连接是否断开，如果断开则重新连接
        self.cur.execute(sql)  # 执行SQL查询语句
        data = self.cur.fetchall()  # 获取查询结果
        logger.info("执行查询语句：%s" % sql)
        return data

    def execute_db(self, sql):
        """更新/新增/删除"""
        if not sql:
            raise ValueError("Empty SQL")  # 抛出值错误异常，SQL语句为空
        try:
            self.conn.ping(reconnect=True)  # 检查数据库连接是否断开，如果断开则重新连接
            self.cur.execute(sql)  # 执行SQL语句
            self.conn.commit()  # 提交事务
            logger.info("执行SQL语句：%s" % sql)
            return f'受影响的行{self.cur.rowcount}'  # 返回受影响的行数
        except Exception as e:
            self.conn.rollback()  # 回滚所有更改
            raise e
        logger.info("执行完毕")
