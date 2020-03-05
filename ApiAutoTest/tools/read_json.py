#coding=utf-8

import json
import os
class LoginJson(object):
    #设置数据文件的路径
    def __init__(self,filename):
        self.filepath = "../data/" + filename
    #读取文件的数据
    def read_json(self):
        with open(self.filepath,"r") as f:
            s = json.load(f)
        return s



if __name__ == '__main__':
    print(LoginJson("login.json").read_json())


