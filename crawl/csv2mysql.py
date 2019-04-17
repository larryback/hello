import pymysql
import csv
import codecs

<<<<<<< HEAD
def get_conn(db):
    return pymysql.connect(
        host='localhost',
        user='dooo',
        password='1234',
=======

def get_conn(db):
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root1!',
>>>>>>> 14b1a64526eeb51aecda34d9ad38c7642b2542db
        port=3306,
        db=db,
        charset='utf8')

<<<<<<< HEAD
# sql_truncate = "truncate table Meltop"
sql_truncate = "delete from Meltop"
sql_insert = "insert into Meltop(rank, title, singer, likecnt) values(%s,%s,%s,%s)"
isStart = True

def save(lst):
    try:
        conn = get_conn('dadb')
        conn.autocommit = False
        cur = conn.cursor()

        global isStart
        if isStart:
            cur.execute(sql_truncate)
            isStart = False

        cur.executemany(sql_insert, lst)
        conn.commit()
        print("Affected RowCount is", cur.rowcount, "/", len(lst))

    except Exception as err:
        try:
            conn.rollback()
        except:
            print("Error on Rollback!!")
            
        print("Error!!", err)

    finally:
        try:
            cur.close()
        except:
            print("Error on close cursor")

        try:
            conn.close()
        except Exception as err2:
            print("Fail to connect!!", err2)


csvFile = codecs.open("../crawl/data/meltop100.csv", "r", "utf-8")
=======
sql_truncate = "truncate table Meltop"
sql_insert = "insert into Meltop(rank, title, singer, likecnt) values(%s,%s,%s,%s)"

csvFile = codecs.open("./melon_top_100.csv", "r", "ms949")
>>>>>>> 14b1a64526eeb51aecda34d9ad38c7642b2542db
reader = csv.reader(csvFile, delimiter=',', quotechar='"')

lst = []
for row in reader:
    lst.append([row[0] , row[1], row[2], row[3]])

print("00>>", lst[0])
print("11>>", lst[1])
del lst[0]
<<<<<<< HEAD
del lst[ len(lst) - 1 ]

save(lst)
=======


conn = get_conn('dadb')
with conn:
    cur = conn.cursor()
    cur.execute(sql_truncate)
    cur.executemany(sql_insert, lst)
    print("Affected RowCount is", cur.rowcount)
>>>>>>> 14b1a64526eeb51aecda34d9ad38c7642b2542db
