#coding=utf-8

import requests

class ApiChannel(object):
    def api_get_channel(self,url,headers):

        #调用get请求
        return requests.get(url,headers=headers)