import bigquery
import sys
import pymysql


conn = pymysql.connect(
        host ='localhost',
        user='dooo',
        password='1234',
        port=3306,
        db='dadb',
        cursorclass=pymysql.cursors.DictCursor,
        charset='utf8')

with conn:

    cur = conn.cursor()

    cur.execute("select * from Song order by songno")  

    s_rows = cur.fetchall()

# for row in s_rows:

#     print(row['songno'], row['title'], row['genre'])    

with conn:

    cur = conn.cursor()

    cur.execute("select * from Album order by albumid")  

    a_rows = cur.fetchall()

for row in a_rows:

    print(row[''], row['title'], row['genre'])            



exit()

client = bigquery.get_client(json_key_file='./bigquery.json', readonly=False)

DATABASE = "bqdb"
TABLE = "Songs"

if not client.check_table(DATABASE, TABLE):
        print("Create table {0}.{1}".format(DATABASE, TABLE), file=sys.stderr)

        # create table
        client.create_table(DATABASE, TABLE, [
                {'name': 'songno', 'type': 'integer', 'description': 'song id'},
                {'name': 'title', 'type': 'string', 'description': 'song title'},
                {'name': 'albumid', 'type': 'string', 'description': 'album id'},
                {'name': 'genre', 'type': 'string', 'description': 'genre title'},
                {'name': 'likecnt', 'type': 'integer', 'description': 'like count'},
                {'name': 'rec', 'type': 'record', 'description': 'record',
                'fields': [ {'name': 'album title', 'type': 'string','description': 'album title'},
                            {'name': 'company', 'type': 'string','description': 'entertainment company'},
                            {'name': 'album likecnt', 'type': 'integer','description': 'album like count'},
                            {'name': 'rate', 'type': 'decimal','description': 'album rating'}]
                },
            ])

