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
    # print(LoginJson("login.json").read_json())
    # datas = LoginJson("login_more.json").read_json()
    # arrs = []
    # for data in datas.values():
    #     arrs.append((data.get("url"),
    #                  data.get("mobile"),
    #                  data.get("code"),
    #                  data.get("except_result"),
    #                  data.get("status_code")))
    # print(arrs)
    datas = LoginJson("channel.json").read_json()
    print(datas)
    arrs = []
    arrs.append((datas.get("url"),
                datas.get("headers"),
                datas.get("except_result"),
                 datas.get("status_code")))
    print(arrs)