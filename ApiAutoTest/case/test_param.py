#coding=utf-8
import unittest
from parameterized import parameterized


class TestParam(unittest.TestCase):

     @parameterized.expand([("chen","111qqq"),("xi","22qqq")])
     def test_param(self,username,password):

         print("用户名"+username)
         print("密码"+password)



# if __name__ == '__main__':
#     unittest.main()