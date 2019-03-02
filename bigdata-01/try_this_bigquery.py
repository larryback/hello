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

<<<<<<< HEAD
with conn:

    cur = conn.cursor()

    cur.execute("select * from Song order by songno")  

    s_rows = cur.fetchall()

# for row in s_rows:

#     print(row['songno'], row['title'], row['genre'])    
=======
# with conn:

#     cur = conn.cursor()

#     cur.execute("select * from Song order by songno")  

#     s_rows = cur.fetchall()

# # for row in s_rows:

# #     print(row['songno'], row['title'], row['genre'])    
>>>>>>> bc0bbb4bf15e08a390da158eaef399fc0a0c9a26

with conn:

    cur = conn.cursor()

<<<<<<< HEAD
    cur.execute("select * from Album order by albumid")  

    a_rows = cur.fetchall()

for row in a_rows:

    print(row[''], row['title'], row['genre'])            



exit()
=======
    cur.execute("select * from (Song s inner join Album a on s.album id = a.album id) order by albumid")  

    rows = cur.fetchall()

for row in rows:

    print(row['songno'], row['title'], row['genre'],row['album id'], row['likecnt'],
    row['title'], row['createdt'], row['company'], row['genre'], row['likecnt'],
    row['rate'], row['crawldt'])            



#exit()
>>>>>>> bc0bbb4bf15e08a390da158eaef399fc0a0c9a26

client = bigquery.get_client(json_key_file='./bigquery.json', readonly=False)

DATABASE = "bqdb"
TABLE = "Songs"

if not client.check_table(DATABASE, TABLE):
        print("Create table {0}.{1}".format(DATABASE, TABLE), file=sys.stderr)

        # create table
        client.create_table(DATABASE, TABLE, [
<<<<<<< HEAD
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

=======
                {'name': 'albumid', 'type': 'string', 'description': 'album id'},
                {'name': 'songno', 'type': 'integer', 'description': 'song id'},
                {'name': 'title', 'type': 'string', 'description': 'song title'},
                {'name': 'genre', 'type': 'string', 'description': 'genre title'},
                {'name': 'likecnt', 'type': 'integer', 'description': 'like count'},
                {'name': 'rec', 'type': 'record', 'description': 'record',
                'fields': [ {'name': 'title', 'type': 'string','description': 'album title'},
                            {'name': 'createdt', 'type': 'string','description': 'album release date'},
                            {'name': 'company', 'type': 'string','description': 'entertainment company'},
                            {'name': 'genre', 'type': 'string','description': 'album genre'},
                            {'name': 'likecnt', 'type': 'integer','description': 'album like count'},
                            {'name': 'rate', 'type': 'decimal','description': 'album rating'},
                            {'name': 'crawldt', 'type': 'string','description': 'crawl date'}]

                },
            ])

Album_Song = "select * from (Song s inner join Album a on s.album id = a.album id) order by albumid"

pushResult = client.push_rows(DATABASE, TABLE, Album_Song, insert_id_key='albumid')
print("Pushed Result is", pushResult)


>>>>>>> bc0bbb4bf15e08a390da158eaef399fc0a0c9a26
