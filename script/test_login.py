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
        # 接收返回的json数据
        jsonData = response.json()
        # 调用输出登录接口返回的数据，日志输出只能用作{}占位
        logging.info('登录成功接口返回的数据为：{}'.format(jsonData))
        # 断言
        # self.assertEqual(200, response.status_code)  # 断言响应状态码
        # self.assertEqual(True, jsonData.get('success'))  # 断言success
        # self.assertEqual(10000, jsonData.get('code'))  # 断言code
        # self.assertIn('操作成功', jsonData.get('message'))  # 断言message
        assert_common(self, response, 200, True, 10000, '操作成功')

    def test02_username_is_not_exist(self):
        # 调用封装的登录接口
        response = self.login_api.login('13500000002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 调用输出登录接口返回的数据，日志输出只能用作{}占位
        logging.info('用户名不存在返回的数据为：{}'.format(jsonData))
        # 断言
        # self.assertEqual(200, response.status_code)  # 断言响应状态码
        # self.assertEqual(False, jsonData.get('success'))  # 断言success
        # self.assertEqual(20001, jsonData.get('code'))  # 断言code
        # self.assertIn('用户名或密码错误', jsonData.get('message'))  # 断言message
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test03_password_error(self):
        # 调用封装的登录接口a
        response = self.login_api.login('13800000002', 'error')
        # 接收返回的json数据
        jsonData = response.json()
        # 调用输出登录接口返回的数据，日志输出只能用作{}占位
        logging.info('密码错误返回的数据为：{}'.format(jsonData))
        # 断言
        # self.assertEqual(200, response.status_code)  # 断言响应状态码
        # self.assertEqual(False, jsonData.get('success'))  # 断言success
        # self.assertEqual(20001, jsonData.get('code'))  # 断言code
        # self.assertIn('用户名或密码错误', jsonData.get('message'))  # 断言message
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test04_username_have_special_char(self):
        # 调用封装的登录接口a
        response = self.login_api.login('@#$%^&', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 输出
        logging.info('手机号存在特殊字符返回的数据为:{}'.format(jsonData))
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test05_username_is_not_empty(self):
        # 调用封装的登录接口a
        response = self.login_api.login('', 'error')
        # 接收返回的json数据
        jsonData = response.json()
        # 输出
        logging.info('账号为空返回的数据为:{}'.format(jsonData))
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test06_password_is_empty(self):
        # 调用封装的登录接口a
        response = self.login_api.login('13800000002', '')
        # 接收返回的json数据
        jsonData = response.json()
        # 输出
        logging.info('密码为空返回的数据为:{}'.format(jsonData))
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test07_usernamr_have_china(self):
        # 调用封装的登录接口a
        response = self.login_api.login('138我00002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 输出
        logging.info('账号存在中文字符返回的数据为:{}'.format(jsonData))
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')

    def test08_usernamr_kongge(self):
        # 调用封装的登录接口a
        response = self.login_api.login('138000 0002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 输出
        logging.info('账号存在空格返回的数据为:{}'.format(jsonData))
        assert_common(self, response, 200, False, 20001, '用户名或密码错误')
