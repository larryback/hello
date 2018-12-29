import pymysql

def get_mysql_conn(db):
    return pymysql.connect(
        host='localhost',
        user='dooo',
        password='dooo!',
        port=3306,
        db=db,
        charset='utf8')

def get_count(conn, tbl, where = ''):
    cur = conn.cursor()
    sql = "select count(*) from " + tbl
    if where != '':
        sql = sql + " where " + where

    # print("get_count.sql=", sql)
    cur.execute(sql)
    return cur.fetchone()[0]

def trunc_table(conn, tbl):
    cur = conn.cursor()
    cur.execute('truncate table ' + tbl)
    return cur.rowcount