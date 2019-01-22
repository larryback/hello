import pymysql
import csv
import codecs

def get_conn(db):
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root1!',
        port=3306,
        db=db,
        charset='utf8')

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

        conn.rollback()
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


csvFile = codecs.open("./melon_top_100.csv", "r", "ms949")
reader = csv.reader(csvFile, delimiter=',', quotechar='"')


lst = []
save_unit = 15
for i, row in enumerate(reader):
    if i != 0 and row[0] != '계':
        lst.append([row[0] , row[1], row[2], row[3]])

    if len(lst) == save_unit or row[0] == '계' :
        save(lst)
        lst.clear()