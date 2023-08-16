# 项目域名
import os
# 基准地址
BASE_HOST = "http://127.0.0.1/"

import logging.handlers
BASE_PATH = os.path.dirname(__file__)

#数据库配置信息
mysql_config={
# MySQL配置
"MYSQL_HOST" :"192.168.89.128",
"MYSQL_PORT" :3306,
"MYSQL_USER":"root",
"MYSQL_PASSWD":"123456",
"MYSQL_DB" :"flask_demo"
}

