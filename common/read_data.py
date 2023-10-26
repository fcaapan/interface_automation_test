import json
from common.logginger import logging
from config import BASE_PATH
import yaml

#读取json文件
def read_json(filename, api_parameters):
    '''
    读取json文件
    :param filename: json文件名，字符串类型
    :param api_parameters: 指定获取api入参的数据
    :return:
    '''
    #打开文件json数据文件
    file_path = BASE_PATH + "/data/" + filename + ".json"
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    #获取指定的数据
    api_data = data.get(api_parameters)
    logging.info("读取原始外部文件测试数据:{}".format(api_data))
    #将指定获取的参数以列表形式返回
    api_list = []
    for api_dict in api_data:
        #以列表嵌套元组形式返回数据
        api_tuple = tuple(api_dict.values())
        api_list.append(api_tuple)
    logging.info("获取的指定api参数：%s" % api_list)
    return api_list


def load_yaml(file_name):
    file_path = BASE_PATH + "/data/" + file_name + ".yaml"

    logging.info("加载 {} 文件......".format(file_path))
    with open(file_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    logging.info("读到数据 ==>>  {} ".format(data))
    return data


print(load_yaml("login_data"))

if __name__ == "__main__":
    # print(read_json('reg_login_data', "img_verify_code"))
    print(read_json('reg_login_data', "user_register"))
