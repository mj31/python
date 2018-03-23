import pymysql
conn = pymysql.connect(host='121.199.20.251', port=3306, user='root', passwd='root', db='bill', charset='utf8')
cursor = conn.cursor()
sql = "SELECT * FROM car_info"
cursor.execute(sql)
resultList = cursor.fetchall()
for result in resultList:
    print(result[2])