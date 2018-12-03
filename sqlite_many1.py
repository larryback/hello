import sqlite3

conn = sqlite3.connect("test.db")

data = (
    (21, '홍길동'),
    (22, '홍길순')
)

with conn:
    cur = conn.cursor()
    sql = "insert into Student(id, name) values(?,?)"
    cur.executemany(sql, data)

    conn.commit()