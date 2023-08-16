# # 1、导包
# from bs4 import BeautifulSoup
#
# data = """
# <html>
#     <head>
#         <title>黑马程序员</title>
#     </head>
#     <body>
#         <p id="test01">软件测试</p>
#         <p id="test02">2020年</p>
#         <a href="/api.html">接口测试</a>
#         <a href="/web.html">Web自动化测试</a>
#         <a href="/app.html">APP自动化测试</a>
# </body>
# </html>
# """
# # 2、获取BeautifulSoup对象
# data =BeautifulSoup(data,parser="html")
# print(data)
# # 3、调用相关方法
# # 获取title标签的全部数据
# title =data.find("title")
#
# # # 获取title标签的内容
# print(title.text,type(title))
#
# # # 获取p标签的第一条数据，id属性的值
# p =data.find("p")
# print(p.get("id"))
# # 获取所有a标签
# a_all =data.find_all("a")
# print(a_all)
# # 获取所有a标签的href属性的值
# a_herf=[]
# for i in a_all:
#     print(i.get("href"))
#     a_herf.append(i.get("href"))
# print(a_herf)
#
# html解析工具
from bs4 import BeautifulSoup
def html_util(response):
    # 1.从响应结果中，获取请求的标签数据
        pass
    # 将获取的标签数据打印到日志

    # 2.创建beautifulsoup对象

    # 3.从form标签中获取url

    # 4. 从input标签中获取请求体数据
    # 4.1 定义一个字典，用来接收请求体的数据

    # 4.2 获取全部的input标签

    # 4.3 循环遍历出每一个input标签

    # 4.4从input标签中获取请求体的字段名

    # 4.5从input标签中获取请求体的字段值

    # 4.6.将字段名和值放入定义的请求体数据的字典中

    # 将提取的请求数据(url和请求体数据)打印到日志
    # 7.返回，带有url和请求体数据的列表
