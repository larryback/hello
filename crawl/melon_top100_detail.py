import requests
from bs4 import BeautifulSoup
import pymysql
import csv
import codecs
import time
import re

#url = "http://vlg.berryservice.net:8099/melon/detail?albumId=10123639"
url = "http://vlg.berryservice.net:8099/melon/list"
  
res = requests.get(url)
html = res.text

soup = BeautifulSoup(html, "html.parser")
trs = soup.select('div#tb_list table tbody tr[data-song-no]')
print(len(trs))
# print(trs[0])


album_data = []

for tr in trs:
    album_json = tr.select('td:nth-of-type(4) a')
    album_title = tr.select_one('div.ellipsis.rank03 a').text
    title = tr.select_one('div.ellipsis.rank01 a').text
    
    for j in album_json:
        strings = j.attrs['href']
        pattern = re.compile("\'(.*)\'")
        album_id = re.findall(pattern, strings)[0]
        #print(album_id)
        album_data.append((album_id, title))


#print(album_data)
#exit()


def get_conn(db):
    return pymysql.connect(
        host= '127.0.0.1',
        user='dooo',
        password='1234',
        port=3307,
        db=db,
        charset='etf8')

#sql_truncate = "truncate table Song"
# sql_insert = "insert into Song(album) values(%s)"
sql_insert = "update Song set album=%s where title=%s"

#csvFile = codecs.open("./melon_top_100.csv", "r", "ms949")
#reader = csv.reader(csvFile, delimiter=',', quotechar='"')

print("00>>", album_data[0])
print("11>>", album_data[1])

conn = get_conn('dooodb')
with conn:
    cur = conn.cursor()
    #cur.execute(sql_truncate)
    for i, data in enumerate(album_data):
        #print(i, data)
        cur.execute(sql_insert, data)
        #cur.executemany(sql_insert, album_data)
    # print("Affected RowCount is", cur.rowcount)
