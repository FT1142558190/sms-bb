import pymysql

# 使用python连接mysql数据库，并对数据库进行添加数据的方法
# 创建连接，数据库主机地址 数据库用户名称 密码 数据库名 数据库端口 数据库字符集编码
conn = pymysql.connect(host='127.0.0.1',
                       user='root',
                       password='dsc770556',
                       database='ft',
                       port=3306,
                       charset='utf8')
print("连接成功")

# 创建游标
cursor = conn.cursor()
#
#
# 添加一条数据数据
# def insertdata1():
#
#     insert_emp_sql = "insert into ft.app01_webo (name,data,time,url) values ('王十八',45,1,3)"
#     # 执行语句
#     cursor.execute(insert_emp_sql)
#     # 提交数据
#     conn.commit()
#     print("ok")
def insertdata(name,data,time,url):
    cursor = conn.cursor()
    insert_emp_sql = "insert into ft.app01_webo (name,data,time,url) values ('{}','{}','{}','{}')"
    ins_sql = insert_emp_sql.format(name,data,time,url)
    print(ins_sql)
    # 执行语句
    cursor.execute(ins_sql)
    # 提交数据
    conn.commit()
    print("ok")

def deleteall():
    cursor = conn.cursor()
    insert_emp_sql = "delete from app01_webo;"
    cursor.execute(insert_emp_sql)
    # 提交数据
    conn.commit()
    print("deleteall()")
# 批量添加数据
# def insertdata2(name,data,time,url):
#     insert_emp_sql = "insert into ft.app01_webo (name,data,time,url) values ('{}',{},1,3);"
#
#     # 插入10条数据0-9
#     for i in range(10):
#         uname = '高少少' + str(i)
#         age = 30 + i
#
#         ins_sql = insert_emp_sql.format(uname, age)
#         cursor.execute(ins_sql)
#         conn.commit()
#
#
# # 删除数据
# def deletedata(id):
#     delete_emp_sql = "delete from ft.app01_webo where eid={}"
#     del_sql = delete_emp_sql.format(id)
#     cursor.execute(del_sql)
#     conn.commit()
#
#
# # 更改数据
# def updatadata():
#     updata_emp_sql = "update ft.app01_webo set age=66 where eid = 26"
#     cursor.execute(updata_emp_sql)
#     conn.commit()
#
#
# 关闭游标跟连接
def closeconn():
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
#
#
# try:
#     deleteall()
#     #insertdata1()
#     # insertdata2()
#     # deletedata(1)
#     # updatadata()
# except:
#     print(conn.rollback())
#
#
# closeconn()
