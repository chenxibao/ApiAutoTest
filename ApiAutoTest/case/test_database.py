#coding=utf-8
import  pymysql

#获取连接对象
conn = pymysql.connect(
    "10.12.9.16","lft_dev","J7HmRdj8","lft_merchant",charset="utf8"
)

#获取游标对象
cursor = conn.cursor()
#执行方法sql
sql = "select * from m_email"

cursor.execute(sql)



#获取结果并进行断言
result = cursor.fetchone()
print(result)

#关闭游标对象
cursor.close()
#关闭连接对象
conn.close()

