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
        album_id = re.findall(pattern, strings)[0]
        #print(album_id)
        album_data.append(album_id)


#print(album_data)
#exit()

lst = []

for i in album_data:

    detail_URL = 'http://vlg.berryservice.net:8099/melon/detail?albumId='+ str(i)
    #print("==========================================================================")
    #print(detail_URL)

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

        rating = s.select_one('span.progress span').text
        #print(rating)
        lst.append((genre, i))
        

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

#sql_truncate = "truncate table Song"
#sql_insert = "insert into Song(album) values(%s)"

for album_id in album_data:

    sql_insert = "update Song set genre=%s where album_id =%s"

    
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

        #exit()
        cur.execute(sql_insert, data)
    # cur.executemany(sql_insert, album_data)
    # print("Affected RowCount is", cur.rowcount)










    # import requests
    # from bs4 import BeautifulSoup
    # from pprint import pprint
    # import json
    # import csv, codecs
    # import re

    # url = "http://vlg.berryservice.net:8099/melon/list"
    # # headers = {
    # #     'Referer': 'https://www.melon.com/',
    # #     'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    # # }
    # trs = mf.request(url).select('tbody tr[data-song-no]')


    # def album_data (trs) :
    #     album_data = []
    #     b = 0
    #     for tr in trs:
    #         album_json = tr.select('td:nth-of-type(4) a')
    #         album_title = tr.select_one('div.ellipsis.rank03 a').text
            
    #         for j in album_json:
    #             strings = j.attrs['href']
    #             pattern = re.compile("\'(.*)\'")
    #             album_id = re.findall(pattern, strings)

    #             print(album_data)

    #             exit()


    # res = requests.get(url)
    # html = res.text

    # soup = BeautifulSoup(html, "html.parser")
    # trs = soup.select('div#tb_list table tbody tr[data-song-no]')
    # print(len(trs))            