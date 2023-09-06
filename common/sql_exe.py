import pymysql

from common.logginger import logger
from config import *
#获取config文件的数据库信息
DB_CONF = {
    "host": mysql_config["MYSQL_HOST"],
    "port": mysql_config["MYSQL_PORT"],
    "user": mysql_config["MYSQL_USER"],
    "password": mysql_config["MYSQL_PASSWD"],
    "db": mysql_config["MYSQL_DB"]
}
logger.info("数据库的配置信息 %s " % DB_CONF)

#测试拆包
# def test(**kwargs):
#     a, b, c, d, e =kwargs
#     print(a,b,c,d,e)
# test(**DB_CONF)
# host port user password db

class MysqlDb():

    def __init__(self, db_conf=DB_CONF):
        # 通过字典拆包传递配置信息，建立数据库连接
        self.conn = pymysql.connect(**db_conf, autocommit=True)
        # 通过 cursor() 创建游标对象，并让查询结果以字典格式输出
        self.cur = self.conn.cursor()

    def __del__(self):  # 对象资源被释放时触发，在对象即将被删除时的最后操作
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()

    def select_db(self, sql):
        """查询"""
        # 检查连接是否断开，如果断开就进行重连
        self.conn.ping(reconnect=True)
        # 使用 execute() 执行sql
        self.cur.execute(sql)
        # 使用 fetchall() 获取查询结果
        data = self.cur.fetchall()
        return data

    def execute_db(self, sql):
        """更新/新增/删除"""
        try:
            # 检查连接是否断开，如果断开就进行重连
            self.conn.ping(reconnect=True)
            # 使用 execute() 执行sql
            self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
            return f'受影响的行{self.cur.rowcount}'
        except Exception as e:
            logger.info("操作MySQL出现错误，错误原因：{}".format(e))
            # 回滚所有更改
            self.conn.rollback()
        logger.info("执行完毕")





