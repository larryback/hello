import pymysql
import csv
import codecs
import time

def get_conn(db):
    return pymysql.connect(
        host='127.0.0.1',
        user='dooo',
        password='1234',
        port=3307,
        db=db,
        charset='utf8')

sql_truncate = "truncate table Song"
sql_insert = "insert into Song(singer, title) values(%s,%s)"

csvFile = codecs.open("./melon_top_100.csv", "r", "ms949")
reader = csv.reader(csvFile, delimiter=',', quotechar='"')

lst = []
for cells in reader:
    #time.sleep(1)
    #print([cells[2], cells[1]])
    print("==================================================================")
    lst.append([cells[2] , cells[1]])

    #lst.append([row[0] , row[1], row[2], row[3]])
    print(lst)

#exit()

print("00>>", lst[0])
print("11>>", lst[1])
del lst[0]


conn = get_conn('dooodb')
with conn:
    cur = conn.cursor()
    cur.execute(sql_truncate)
    cur.executemany(sql_insert, lst)
    print("Affected RowCount is", cur.rowcount)