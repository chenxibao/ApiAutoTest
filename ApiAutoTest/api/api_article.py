#coding=utf-8
import requests

class ApiArticle(object):
    def api_post_collection(self,url,headers,data):

        return requests.post(url,headers=headers,json=data)

    def api_delete_article(self,url,headers):

        return requests.delete(url,headers=headers)
