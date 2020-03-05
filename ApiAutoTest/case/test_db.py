#coding=utf-8
import unittest
from tools.read_db import ReadBD

class TestDB(unittest.TestCase):

    def test_db(self):
        sql = "select * from m_email"

        data = ReadBD().get_sql_one(sql)
        print(data[0])

        self.assertEquals(4,data[0])

if __name__ == '__main__':
    unittest.main()