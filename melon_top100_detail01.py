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

pattern = re.compile("\'(.*)\'")
# pattern = re.compile('(\d)')
def getNum(str):
    return re.findall(pattern, str)[0]



album_data = []

for tr in trs:
    album_json = tr.select('td:nth-of-type(4) a')
    album_title = tr.select_one('div.ellipsis.rank03 a').text
    title = tr.select_one('div.ellipsis.rank01 a').text
    #print(title)
    
    for j in album_json:
        strings = j.attrs['href']
        pattern = re.compile("\'(.*)\'")
        album = re.findall(pattern, strings)[0]
        #print(album)
        album_data.append(album)


#print(album_data)
#exit()

lst = []

for album in album_data:

    detail_URL = 'http://vlg.berryservice.net:8099/melon/detail?albumId='+ str(album)
    #print("==========================================================================")
    #print(detail_URL)

    #exit()

    res = requests.get(detail_URL)
    html = res.text
    soup = BeautifulSoup(html, "html.parser")
    ss = soup.select('#conts > div.section_info > div')
    #print("===================================================")
    #print(ss)


    for s in ss:

        albums = s.select_one('div.song_name').text
        abm = albums[4:]
        album = abm.strip()
        #print(album)
        genre = s.select_one('div.meta dl dd:nth-of-type(2)').text
        #print(genre)
        label = s.select_one('div.meta dl dd:nth-of-type(3)').text
        #print(label)
        #exit()
        rating = s.select_one('span.progress span').text
        #print(rating)
        lst.append((rating, label))

        
        



#print(lst)

#exit()


def get_conn(db):
    return pymysql.connect(
        host='34.85.46.200',
        user='root',
        password='root1!',
        port=3306,
        db=db,
        charset='utf8')

sql_truncate = "truncate table Album"
sql_insert = "insert into Album(rating, label) values(%s,%s)"



#sql_insert = "update Song set genre=%s where album =%s"

    
#csvFile = codecs.open("./melon_top_100.csv", "r", "ms949")
#reader = csv.reader(csvFile, delimiter=',', quotechar='"')

print("00>>", lst[0])
print("11>>", lst[1])

conn = get_conn('melondb')
with conn:
    cur = conn.cursor()
    #cur.execute(sql_truncate)
    for i, data in enumerate(lst):
        print(i, data)
        cur.execute(sql_insert, data)
    # cur.executemany(sql_insert, album_data)
    # print("Affected RowCount is", cur.rowcount)









    