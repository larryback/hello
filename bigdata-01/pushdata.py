import bigquery
import sys
client = bigquery.get_client(json_key_file='./bigquery.json', readonly=False)

DATABASE = "bqdb"
TABLE = "test"
if not client.check_table(DATABASE, TABLE):
    print("Create table {0}.{1}".format(DATABASE, TABLE), file=sys.stderr)

    client.create_table(DATABASE, TABLE, [
        {'name': 'songno', 'type': 'string', 'description': 'song id'},
        {'name': 'title', 'type': 'string', 'description': 'song title'},
        {'name': 'albumid', 'type': 'string', 'description': 'album id'},
    ])

ttt = [
    # {'songno': '111', 'title': '홍1', 'albumid': '121212121'},
    {'songno': '222', 'title': '홍2', 'albumid': '121212121'},
    {'songno': '333', 'title': '홍3', 'albumid': '121212121'},
 ]
pushResult = client.push_rows(DATABASE, TABLE, ttt, insert_id_key='songno')
<<<<<<< HEAD
<<<<<<< HEAD
print("Pushed Result is", pushResult)
=======
print("Pushed Result is", pushResult)

>>>>>>> bc0bbb4bf15e08a390da158eaef399fc0a0c9a26
=======
print("Pushed Result is", pushResult)

>>>>>>> 4236b33dbf30ad9b102df643cbc7d665f242f348
