import pymysql


conn = pymysql.connect(host='localhost',
                       port=3308,
                       user='admin',
                       password='exodus',
                       database='movies')
