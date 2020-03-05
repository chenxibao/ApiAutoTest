#coding=utf-8
from tools.HTMLTestRunner import HTMLTestRunner
import time
import unittest


#第一步组装测试套件
suite = unittest.defaultTestLoader.discover("./case",pattern="test*.py")

#指定报告存放路径及文件
file_path = "./report/{}.html".format(time.strftime("%Y-%m-%d %H-%M-%S"))

#第三步运行套件，并生成测试报告

with open(file_path,'w')  as f :
    HTMLTestRunner(stream=f).run(suite)
