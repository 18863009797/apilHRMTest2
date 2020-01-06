import logging
import unittest
from api.emp_api import Emapi
from utils import assert_common, DBUtils
import app
from parameterized.parameterized import parameterized
from utils import read_add_emp_data, read_query_emp_data, read_modify_emp_data, read_delete_emp_data
import pymysql


class TestIHRMEmp(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        # 初始化员工类
        cls.emp_api = Emapi()

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    @parameterized.expand(read_add_emp_data)
    def test01_add_emp(self, username, mobile, success, code, message, http_code):
        # 调用添加员工接口
        response = self.emp_api.add_emp(username, mobile)
        # 获取添加员工接口的json数据
        jsonData = response.json()
        # 输出json数据
        logging.info("添加员工接口返回数据为：{}".format(jsonData))
        # 获取员工ID保存在全局变量
        app.EMP_ID = jsonData.get("data").get("id")
        logging.info("员工ID： {}".format(app.EMP_ID))
        # 断言
        assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(read_query_emp_data)
    def test02_query_emp(self, success, code, message, http_code):
        # 调用查询员工接口
        response = self.emp_api.query_emp()
        # 获取查询员工接口的返回json数据
        jsonData = response.json()
        # 输出json数据
        logging.info("查询员工接口的返回数据为:{}".format(jsonData))
        # 断言
        assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(read_modify_emp_data)
    def test03_modify_emp(self, username, success, code, message, http_code):
        # 调用修改员工接口
        response = self.emp_api.modify_emp(username)
        # 获取修改员工接口的返回json数据
        jsonData = response.json()
        # 输出json数据
        logging.info("修改员工接口的返回数据为:{}".format(jsonData))

        with DBUtils()as db_utils:
            # 执行查询语句，查询修改之后的username
            sql = 'select username from bs_user where id={}'.format(app.EMP_ID)
            db_utils.execute(sql)
            # 获取执行结果
            result = db_utils.fetchone()[0]
            logging.info('从数据库中查询的员工的用户名是:{}'.format(result))
        # 建立连接
        conn = pymysql.connect("182.92.81.159", 'readuser', 'iHRM_user_2019', 'ihrm')
        # 获取游标
        cursor = conn.cursor()
        # 执行查询语句，查询出添加的员工的username是不是修改的username
        sql = "select username from bs_user where id={}".format(app.EMP_ID)
        cursor.execute(sql)
        # 获取执行结果
        result = cursor.fetchone()[0]
        logging.info("从数据库中查询出的员工的用户名是：{}".format(result))
        # self.assertEqual(username, result)
        # cursor.close()
        # conn.close()
        #
        # with DBUtils() as db_utils:
        #     db_utils.execute("select username from bs_user where id={}".format(app.EMP_ID))
        #     logging.info(db_utils.fetchone())

        # 断言
        assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(read_delete_emp_data)
    def test04_delete_emp(self, success, code, message, http_code):
        # 调用删除员工接口
        response = self.emp_api.delete_emp()
        # 获取修改员工接口的返回json数据
        jsonData = response.json()
        # 输出json数据
        logging.info("删除员工接口的返回数据为:{}".format(jsonData))
        # 断言
        assert_common(self, response, http_code, success, code, message)
