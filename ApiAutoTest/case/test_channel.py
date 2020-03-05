#coding=utf-8

import unittest
from api.api_channels import ApiChannel
from tools.read_json import LoginJson
from parameterized import parameterized

def get_data():
    datas = LoginJson("channel.json").read_json()
    arrs = []
    arrs.append((datas.get("url"),
                 datas.get("headers"),
                 datas.get("except_result"),
                 datas.get("status_code")))
    return arrs

class TestChannels(unittest.TestCase):
    #测试用例
    @parameterized.expand(get_data())
    def test_channels(self,url,headers,except_result,status_code):
        # url = "http://ttapi.research.itcast.cn/app/v1_0/user/channels"
        # headers = {"Content-type":"application/json",
        #            "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODMzNDI4MTIsInVzZXJfaWQiOjEyMzUwNTk1Mzc0NjQwMDA1MTIsInJlZnJlc2giOmZhbHNlfQ.3Bz75-GkD9vpJba4El79pIi2dGQfLVqIziZwrmUpoKc"}
        r = ApiChannel().api_get_channel(url,headers)
        print(r.json)

        self.assertEquals(status_code,r.status_code)
        self.assertEquals(except_result,r.json()["message"])

#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODMzNDI4MTIsInVzZXJfaWQiOjEyMzUwNTk1Mzc0NjQwMDA1MTIsInJlZnJlc2giOmZhbHNlfQ.3Bz75-GkD9vpJba4El79pIi2dGQfLVqIziZwrmUpoKc', 'refresh_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9

if __name__ == '__main__':
    unittest.main()