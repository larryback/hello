import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import csv, codecs
import re
import pymysql


#url = "https://www.melon.com/chart/index.htm"
url = "http://vlg.berryservice.net:8099/melon/list"

    # heads = {
    #     "Referer": "https: // www.melon.com/chart/index.htm",
    #     "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    # }

#res = requests.get(url, headers=heads)

res = requests.get(url)
html = res.text

soup = BeautifulSoup(html, "html.parser")
trs = soup.select('div#tb_list table tbody tr[data-song-no]')
print(len(trs))
#print(trs[0])


#exit()

pattern = re.compile("\'(.*)\'")
# pattern = re.compile('(\d)')
def getNum(str):
    return re.findall(pattern, str)[0]


   

dic = []  #{} # { song_no: {title:'...', singer: '...' } }

for tr in trs:
    song_no = tr.attrs['data-song-no']
    ranking = tr.select_one('span.rank').text
    title = tr.select_one('div.ellipsis.rank01 a').text
    # singers = tr.select('div.ellipsis.rank02 a')
    singers = tr.select('div.ellipsis.rank02 span a')
    singer = ",".join([a.text for a in singers])
    album = getNum(tr.select_one('div.ellipsis.rank03 a').get('href'))
    #print("==========================================================================")
    #print(album)
    #exit()
    dic.append((ranking, title, singer))
    #dic[song_no] = {'ranking': int(ranking), 'title':title, 'singer': singer}

    detail_URL = 'http://vlg.berryservice.net:8099/melon/detail?albumId='+ str(album)
        # print("==========================================================================")
        # print(detail_URL)

        # exit()
    
    res = requests.get(detail_URL)
    html = res.text
    soup = BeautifulSoup(html, "html.parser")
    trs = soup.select('#conts > div.section_info > div')
        # print("===================================================")
        # print(trs)


    for tr in trs:
        albums = tr.select_one('div.song_name').text
        abm = albums[4:]
        album = abm.strip()
        #print(album)
        genre = tr.select_one('div.meta dl dd:nth-of-type(2)').text
        #print(genre)

        rating = tr.select_one('span.progress span').text
        #print(rating)
      

#exit()



#exit()
#print(dic)

likeUrl = "http://vlg.berryservice.net:8099/melon/likejson"
    # likeParams = {
    #     "contsIds": ",".join(dic.keys())
    # }

#resLikecnt = requests.get(likeUrl, headers=heads, params=likeParams)
resLikecnt = requests.get(likeUrl)
#print(resLikecnt.url)
#exit()
jsonData = json.loads(resLikecnt.text)
#pprint(jsonData)
#exit()
for j in jsonData['contsLike']:
    key = str(j['CONTSID'])
    songDic = dic[key]
    songDic['likecnt'] = j['SUMMCNT']
    songDics = songDic['likecnt']

    print("-------------------------------------------------------------------")
    #print(a)
    #print(j["SUMMCNT"])
    print(songDic["likecnt"])
exit()


result = sorted(dic.items(), key=lambda d: d[1]['ranking'])
sortLike = sorted(dic.items(), key=lambda d: d[1]['likecnt'])

print("-----------------------------------------------------------")
pprint(result[1])
print("------------------------------------------------------------")
pprint(sortLike[0])

leastLike = sortLike[0][1]["likecnt"] 

pprint(leastLike)

# fp = codecs.open("./melon_top_100.csv", "r", "utf-8")

# # aaa,bbb,"ccc,cc"
# reader = csv.reader(fp, delimiter=',', quotechar='"')






def get_conn(db):
    return pymysql.connect(
        host='34.85.46.200',
        user='Dooo',
        password='1234',
        port=3306,
        db=db,
        charset='utf8')

sql_truncate = "truncate table Song"
sql_insert = "insert into Song(ranking, title, singer ) values(%s,%s,%s)"

conn = get_conn('melondb')
with conn:
    cur = conn.cursor()
    #cur.execute(sql_truncate)
    for i, data in enumerate(dic):
        print(i, data)
        cur.execute(sql_insert, data)







    # with codecs.open('./crawl/melon_top_100_01.csv', 'w', 'ms949') as ff:

    #     writer = csv.writer(ff, delimiter=',', quotechar='"')

    #     writer.writerow(['랭킹', '제목', '가수', '앨범', '좋아요', '좋아요차이'])
    #     #writer.writerow


    #     likesum = 0
    #     diffsum = 0

    #     for i in result:
    #         song = i[1]
    #         rank = song['ranking']
    #         title = song['title']
    #         singer = song['singer']
    #         album = song['album']
    #         likecnt = song['likecnt']
    #         likeDiff = likecnt - leastLike
    #         likesum = likesum + likecnt
    #         diffsum = diffsum + likeDiff
    #         l =[rank, title, singer, likecnt, likeDiff]
    #         writer.writerow(l)