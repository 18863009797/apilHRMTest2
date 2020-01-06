import requests
import app


class LoginApi():
    def __init__(self):
        self.login_url = app.HOST + '/api/sys/login'
        self.headers = app.HEADERS
        # 从外部接受mobile和password
        # 这样写，如果写成一个参数data来接收
        # 字典数据的话
        # 那么后续进行参数化时，会不方便，所以改成两个接收

    def login(self, mobile, password):
        # 使用data来接收外部传入的mobile和password，拼接成要发送的数据
        data = {"mobile": mobile, "password": password}
        # 发送登录请求
        response = requests.post(self.login_url, json=data, headers=self.headers)
        # 返回响应数据
        return response
