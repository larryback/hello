import pymysql
import cx_Oracle

<<<<<<< HEAD
def get_oracle_conn(usr, usrpw, localhost):
        return cx_Oracle.connect(usr, usrpw, localhost)

=======
def get_oracle_conn():
    return cx_Oracle.connect("hr", "hrpw", "localhost:1521/xe")
    
>>>>>>> 1424f321792e1638f64846d1c494b72adfbc3a83
def get_mysql_conn(db):
    return pymysql.connect(
        host='localhost',
        user='dooo',
<<<<<<< HEAD
        password='1234',
=======
        password='dooo!',
>>>>>>> 1424f321792e1638f64846d1c494b72adfbc3a83
        port=3306,
        db=db,
        charset='utf8')

<<<<<<< HEAD
=======

>>>>>>> 1424f321792e1638f64846d1c494b72adfbc3a83
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
<<<<<<< HEAD
    return cur.rowcount
=======
    return cur.rowcount
>>>>>>> 1424f321792e1638f64846d1c494b72adfbc3a83
