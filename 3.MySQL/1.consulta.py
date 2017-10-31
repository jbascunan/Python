import pymysql

conn = pymysql.connect(host='localhost',
                       port=3308,
                       user='admin',
                       password='exodus',
                       database='movies')

cur = conn.cursor()
cur.execute("select * from movie")

# print(cur.description)

for row in cur:
    print(row)

cur.close
conn.close
