import requests
import app


class Emapi:
    def __init__(self):
        self.emp_url = app.HOST + '/api/sys/user'
        self.henders = app.HEADERS

    def add_emp(self, username, mobile):
        data = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2020-01-06",
            "formOfEmployment": 1,
            "workNumber": "1234",
            "departmentName": "测试",
            "departmentId": "1210411411066695680",
            "correctionTime": "2020-01-28T16:00:00.000Z"

        }
        # 发送添加yuang接口请求
        response = requests.post(self.emp_url, json=data, headers=self.henders)

        return response
        # 封装员工查询接口

    def query_emp(self):
        # 查询员工的URL结构是http://182.92.159/api/sys/user/12345678889
        # 拼接URL加上'/'
        url = self.emp_url + "/" + app.EMP_ID
        # 返回查询的结果，headers是{'Content-Type':'application','Authorization'：'Bearer xxxx'}
        return requests.get(url, headers=self.henders)

    def modify_emp(self, username):
        # 修改员工的URL应该和查询员工是一样的   拼接URL加上'/'
        url = self.emp_url + '/' + app.EMP_ID
        # 从外部接收修改的username，拼接成json数据
        data = {'username': username}
        # 返回查询结果
        return requests.put(url, json=data, headers=self.henders)

    def delete_emp(self):
        url=self.emp_url+'/'+app.EMP_ID
        return requests.delete(url,headers=self.henders)