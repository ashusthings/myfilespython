import pymysql
sql_conn =pymysql.connect(user="root",password=" ",host='localhost')
print(sql_conn)

#sql_cur = sql_conn.cursor() #will create cursor inside the connection

#print(sql_cur.exxecute('show databases'))

#print(sql_cur.fetchall())# will return all the data it fetch during cursor eecution

#sql_cur.execute('create database emp_info')

#sql_conn.close()# closing the connection with the database

