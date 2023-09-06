from flask import Flask, jsonify, request

#创建应用对象
app =Flask(__name__)
#      mock登入请求路径，       mock登入接口的请求方法
@app.route("/login",methods =["get","post"])#一个接口有多个请求方法
#接口返回响应的响应体数据
def login():
    data ={"success":True,"code":10000,"message":"操作成功","data":"......"}
    #将字典转换为字符串
    return jsonify(data)
def login_1():
    params =request.form.get("p")
    if params =="a":
        data = {"success": True, "code": 10000, "message": "操作成功", "data": "......"}
    elif params == "b":
        data = {"success": False, "code": 20001, "message": "用户名或密码错误", "data": "......"}
    else:
        data = {"success": False, "code": 99999, "message": "服务器超时", "data": "......"}
    return jsonify(data)

if __name__ =="__main__":
    app.run()