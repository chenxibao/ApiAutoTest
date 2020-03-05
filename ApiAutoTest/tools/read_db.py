#coding=utf-8
#导包操作
import pymysql
#新建工具类 数据库
class ReadBD:
    conn = None

    #获取连接对象方法封装
    def get_conn(self):
        if self.conn is None:
            self.conn = pymysql.connect("10.12.9.16","lft_dev","J7HmRdj8","lft_merchant",charset="utf8")

        return self.conn

    #获取游标对象方法封装
    def get_cursor(self):
        return self.get_conn().cursor()
    #关闭游标对象封装
    def close_cursor(self,cursor):
        if cursor:
            cursor.close()

    #关闭连接对象封装
    def close_conn(self):
        if self.conn:
            self.conn.close()
            #注意：关闭连接对象后，对象还存在内存中，需要手动设置为None
            self.conn= None

    #主要执行方法
    def get_sql_one(self,sql):
        #定义游标对象即数据变量
        surser = None
        data = None
        try:
                #获取游标对象
            surser = self.get_cursor()
            print(surser)
                #调用执行方法
            print(surser.execute(sql))
                #获取结果
            data = surser.fetchone()
            print(data)
        except Exception as e:
            print("get_sql_one error")
        finally:
                #关闭游标对象
            self.close_cursor(surser)
                #关闭连接对象
            self.close_conn()
                #返回执行结果
            return data

if __name__ == '__main__':
    sql = "select * from m_email"
    print(ReadBD().get_sql_one(sql))