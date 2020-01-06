import unittest, logging

from api.login_api import LoginApi
from utils import assert_common, read_login_data
from parameterized.parameterized import parameterized


class TestIHRMLoginPara(unittest.TestCase):
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

    @parameterized.expand(read_login_data)
    def test_login(self, mobile, password, http_code, success, code, message):
        # 调用封装的登录接口
        response = self.login_api.login(mobile, password)
        # 接收返回的json数据
        jsonData = response.json()
        # 调用输出登录接口返回的数据，日志输出只能用作{}占位
        logging.info('登录成功接口返回的数据为：{}'.format(jsonData))
        assert_common(self, response, http_code, success, code, message)
