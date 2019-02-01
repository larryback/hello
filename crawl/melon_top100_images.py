import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import csv, codecs
import urllib.request
import urls
import urllib.parse as parse
import os.path as path



url = "https://www.melon.com/chart/index.htm#params%5Bidx%5D=1"

heads = {
    "Referer": "https: // www.melon.com/chart/index.htm",
    "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

res = requests.get(url, headers=heads)
html = res.text

soup = BeautifulSoup(res.text, "html.parser")

sel = "#lst50 > td > div > a > img"

imgs = soup.select(sel)
# print(imgs, len(imgs))

if len(imgs) < 1:
    exit()

print("--------------------------------------")
for img in imgs:
    src = img.get('src')
    print("img>>", src)
    with open("./images/" + urls.getFilename(src), "wb") as file:
        file.write(requests.get(src).content)



url = "https://www.melon.com/chart/index.htm#params%5Bidx%5D=51"

sel = "#lst50 > td > div > a > img"

imgs = soup.select(sel)
# print(imgs, len(imgs))

if len(imgs) < 1:
    exit()

print("--------------------------------------")
for img in imgs:
    src = img.get('src')
    print("img>>", src)
    with open("./images/" + urls.getFilename(src), "wb") as file:
        file.write(requests.get(src).content)






























    # trs = soup.select('div#tb_list table tbody tr[data-song-no]')
    # print(len(trs))
    # # print(trs[0])

    # dic = {}   # { song_no: {title:'...', singer: '...' } }

    # for tr in trs:
    #     song_no = tr.attrs['data-song-no']
    #     ranking = tr.select_one('span.rank').text
    #     title = tr.select_one('div.ellipsis.rank01 a').text
    #     # singers = tr.select('div.ellipsis.rank02 a')
    #     singers = tr.select('div.ellipsis.rank02 span a')
    #     singer = ",".join([a.text for a in singers])
    #     dic[song_no] = {'ranking': int(ranking), 'title':title, 'singer': singer}

    #     nametemp = soup.get('alt')
    #     filename = nametemp

    #     for img in tr.findAll('img'):
    #         print(img.get('src'))
    #         imagefile = open('filename' + 'png', 'wb')
    #         imagefile.write(urllib.request.urlopen(img.get('src')).read())
    #         imagefile.close()
        

    # likeUrl = "https://www.melon.com/commonlike/getSongLike.json"
    # likeParams = {
    #     "contsIds": ",".join(dic.keys())
    # }

    # resLikecnt = requests.get(likeUrl, headers=heads, params=likeParams)
    # # print(resLikecnt.url)
    # jsonData = json.loads(resLikecnt.text)
    # # pprint(jsonData)
    # for j in jsonData['contsLike']:
    #     key = str(j['CONTSID'])
    #     songDic = dic[key]
    #     songDic['likecnt'] = j['SUMMCNT']
    #     songDics = songDic['likecnt']




    #     #print("-------------------------------------------------------------------")
    #     #print(a)
    #     #print(j["SUMMCNT"])
    #     #print(songDic["likecnt"])

    # result = sorted(dic.items(), key=lambda d: d[1]['ranking'])
    # sortLike = sorted(dic.items(), key=lambda d: d[1]['likecnt'])

    # print("-----------------------------------------------------------")
    # pprint(result[1])
    # print("------------------------------------------------------------")
    # pprint(sortLike[0])

    # leastLike = sortLike[0][1]["likecnt"] 

    # pprint(leastLike)

    # # fp = codecs.open("./melon_top_100.csv", "r", "utf-8")

    # # # aaa,bbb,"ccc,cc"
    # # reader = csv.reader(fp, delimiter=',', quotechar='"')

    # with codecs.open('./melon_top_100_with_images.csv', 'w', 'ms949') as ff:

    #     writer = csv.writer(ff, delimiter=',', quotechar='"')

    #     writer.writerow(['랭킹', '제목', '가수', '좋아요', '좋아요차이', '사진'])
    #     #writer.writerow
        
        
    #     likesum = 0
    #     diffsum = 0
        
    #     for i in result:
    #         song = i[1]
    #         rank = song['ranking']
    #         title = song['title']
    #         singer = song['singer']
    #         likecnt = song['likecnt']
    #         likeDiff = likecnt - leastLike
    #         likesum = likesum + likecnt
    #         diffsum = diffsum + likeDiff
    #         #image = image

    #         l =[rank, title, singer, likecnt, likeDiff]
    #         writer.writerow(l)

