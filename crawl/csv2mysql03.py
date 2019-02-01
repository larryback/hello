import pymysql
import csv
import codecs
import time

def get_conn(db):
    return pymysql.connect(
<<<<<<< HEAD
        host='127.0.0.1',
        user='dooo',
        password='1234',
        port=3307,
=======
        host='34.85.46.200',
        user='root',
        password='root1!',
        port=3306,
>>>>>>> 14b1a64526eeb51aecda34d9ad38c7642b2542db
        db=db,
        charset='utf8')

sql_truncate = "truncate table Song"
<<<<<<< HEAD
sql_insert = "insert into Song(singer, title) values(%s,%s)"
=======
sql_insert = "insert into Song(title, singer) values(%s,%s)"
>>>>>>> 14b1a64526eeb51aecda34d9ad38c7642b2542db

csvFile = codecs.open("./melon_top_100.csv", "r", "ms949")
reader = csv.reader(csvFile, delimiter=',', quotechar='"')

lst = []
for cells in reader:
    #time.sleep(1)
<<<<<<< HEAD
    #print([cells[2], cells[1]])
    print("==================================================================")
    lst.append([cells[2] , cells[1]])
=======
    #print([cells[1], cells[2]])
    print("==================================================================")
    lst.append([cells[1] , cells[2]])
>>>>>>> 14b1a64526eeb51aecda34d9ad38c7642b2542db

    #lst.append([row[0] , row[1], row[2], row[3]])
    print(lst)

#exit()

print("00>>", lst[0])
print("11>>", lst[1])
del lst[0]


<<<<<<< HEAD
conn = get_conn('dooodb')
=======
conn = get_conn('melondb')
>>>>>>> 14b1a64526eeb51aecda34d9ad38c7642b2542db
with conn:
    cur = conn.cursor()
    cur.execute(sql_truncate)
    cur.executemany(sql_insert, lst)
    print("Affected RowCount is", cur.rowcount)