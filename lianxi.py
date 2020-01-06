# # 编写断言代码函数
# import json
#
# import app
#
#
# def assert_common(self, response, http_code, success, code, message):
#     self.assertEqual(http_code, response.status_code)  # 断言响应状态码
#     self.assertEqual(success, response.json().get('success'))  # 断言success
#     self.assertEqual(code, response.json().get('code'))  # 断言code
#     self.assertIn(message, response.json().get('message'))  # 断言message
#
# def read_login_data():
#     data_path=app.BASE_DIR+'/data/login_data.json'
#     with open(data_path,mode='r',encoding='utf-8')as f:
#         # 加载文件为json格式的数据
#         jsonData=json.load(f)
#         # 遍历文件取出其中数据并保存在列表中
#         p_list=[]
#         for data in jsonData:
#             mobile=data.get('mobile')
#             password=data.get('password')
#             http_code=data.get('http_code')
#             success=data.get('success')
#             code=data.get('code')
#             message=data.get('message')
#             p_list.append(mobile,password,http_code,success,code,message)
#         print(p_list)
#         return p_list
# if __name__ == '__main__':
#     # main函数的作用
#     # 防止调用这个模块或者类时，自动执行代码
#     read_login_data()

import unittest, logging

from api.login_api import LoginApi
from utils import assert_common


class TestIHRMLogin(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        # 初始化登录类
        cls.login_api = LoginApi()

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test01_login_success(self):
        # 调用封装的登录接口
        response = self.login_api.login('13800000002', '123456')
        # 接口返回的json数据
        jsonData = response.json()
        # 调用输入登录接口返回的数据，日志输出只能用作{}占位
        logging.info('登录成功接口返回的数据为:{}'.format(jsonData))
        # 断言
        assert_common(self, response, 200, True, 10000, '操作成功')

    def test02_username_is_not_exist(self):
        # 调用封装的登录接口
        response = self.login_api.login('13200000002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 调用输出登录返回的数据,日志输出只能用做{}占位
        logging.info('用户名不存在返回的数据为:{}'.format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test03_password_error(self):
        response = self.login_api.login('13800000002', 'error')
        # 接收返回的json数据
        jsonData = response.json()
        logging.info('密码错误返回的数据为:{}'.format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test04_username_have_special_char(self):
        response = self.login_api.login('#$%^&', '123456')
        jsonData = response.json()
        logging.info('手机号存在特殊字符返回的数据为:{}'.format(jsonData))
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test05_username_is_not_empty(self):
        response = self.login_api.login('', 'error')
        jsonData = response.json()
        logging.info('账号为空返回的数据为:{}'.format(jsonData))
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test06_password_is_empty(self):
        response = self.login_api.login('13800000002', '')
        jsonData = response.json()
        logging.info('密码为空返回的数据为:{}'.format(jsonData))
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test07_username_have_china(self):
        response = self.login_api.login('138000我你999', '123456')
        jsonData = response.json()
        logging.info('账号存在中文字符返回的数据为:{}'.format(jsonData))
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')
