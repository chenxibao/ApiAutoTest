#coding=utf-8

import requests

class ApiLogin(object):

    def api_post_login(self,url,mobile,code):
        #请求头header
        headers = {"Content-type":"application/json"}
        data = {"mobile":mobile,"code":code}
        #用json的格式就你行请求
        return requests.post(url,headers=headers,json=data)