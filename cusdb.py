import mysql.connector as mysql
con=mysql.connect(host='localhost',user='root',passwd='',database='amazon')
cursor=con.cursor()
cursor.execute('select * from customer')
rows=cursor.fetchall()
for i in rows:
    print('cusid',i[0])
    print('cusname',i[1])
    print('gender',i[2])
    print('mailid',i[4])
