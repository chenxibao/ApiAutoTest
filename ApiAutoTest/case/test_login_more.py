#coding=utf-8

from api.api_login import ApiLogin
import unittest
from tools.read_json import LoginJson
from parameterized import parameterized

def get_data():
    datas = LoginJson("login_more.json").read_json()
    arrs = []
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("mobile"),
                     data.get("code"),
                     data.get("except_result"),
                     data.get("status_code")))
    return arrs

class TestLogin(unittest.TestCase):

    @parameterized.expand(get_data())
    def test_login(self,url,mobile,code,except_result,status_code):
        #暂时存放url,mobile,code
        # url = "http://ttapi.research.itcast.cn/app/v1_0/authorizations"
        # mobile = "18618456564"
        # code = ""
        #调用登录方法
        s = ApiLogin().api_post_login(url,mobile,code)
        #查看响应结果
        print(s.json())
        #断言设置 响应信息及状态码
        self.assertEquals(except_result,s.json()["message"])
        #断言响应状态码
        # status_code
        self.assertEquals (status_code,s.status_code)

if __name__ == '__main__':
    #执行测试用用例
    unittest.main()


