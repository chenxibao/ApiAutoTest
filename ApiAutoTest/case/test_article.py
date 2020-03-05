#coding=utf-8
import unittest
from api.api_article import ApiArticle
from tools.read_json import LoginJson
from parameterized import parameterized

def get_data_collection():
    datas = LoginJson("collection.json").read_json()
    arrs = []
    arrs.append((datas.get("url"),
                 datas.get("headers"),
                 datas.get("data"),
                 datas.get("status_code")))
    return arrs

def get_data_cancel():
    datas = LoginJson("cancel.json").read_json()
    arrs = []
    arrs.append((datas.get("url"),
                 datas.get("headers"),
                 datas.get("status_code")))
    return arrs

class TestArticle(unittest.TestCase):

    @parameterized.expand(get_data_collection())
    def test01_collection(self,url,headers,data,status_code):

        # url = "http://ttapi.research.itcast.cn/app/v1_0/article/collections"
        # headers = {"Content-type":"application/json","Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODMzNDI4MTIsInVzZXJfaWQiOjEyMzUwNTk1Mzc0NjQwMDA1MTIsInJlZnJlc2giOmZhbHNlfQ.3Bz75-GkD9vpJba4El79pIi2dGQfLVqIziZwrmUpoKc"}
        # data = {"target":1}


        r = ApiArticle().api_post_collection(url,headers,data)
        print(r)

        # self.assertEquals("OK",r.json()["message"])

        self.assertEquals(status_code,r.status_code)

    @parameterized.expand(get_data_cancel())
    def test02_cancel(self,url,headers,status_code):
        # url = "http://ttapi.research.itcast.cn/app/v1_0/article/collections/1"
        # headers = {"Content-type":"application/x-www-form-urlencoded","Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODMzNDI4MTIsInVzZXJfaWQiOjEyMzUwNTk1Mzc0NjQwMDA1MTIsInJlZnJlc2giOmZhbHNlfQ.3Bz75-GkD9vpJba4El79pIi2dGQfLVqIziZwrmUpoKc"}

        r = ApiArticle().api_delete_article(url,headers)

        # self.assertEquals("OK",r.json()["message"])
        self.assertEquals(status_code,r.status_code)

if __name__ == '__main__':
    unittest.main()