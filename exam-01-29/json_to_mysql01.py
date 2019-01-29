import requests, json
from bs4 import BeautifulSoup
import pymysql
import csv
import codecs
import time
import re

headers = {
    "X-Naver-Client-Id": "DJp53oSwPDBoa8kGI4tB",
    "X-Naver-Client-Secret": "VCL3gyA7wH"
}

# title = "Python"
title = "파이썬"

params = {
    "display": 100,
    "start": 1,
    "sort": "date",
    "query": title
   
}

#items = {
 #   "title":"title",
 #   "link":"link",
 #   "bloggername":"bloggername",
 #   "postdate":"postdate"
 #   }


# url = "https://openapi.naver.com/v1/search/book.json"
url = "https://openapi.naver.com/v1/search/blog"
# url = "https://openapi.naver.com/v1/search/image"
html = requests.get(url, params=params, headers=headers).text
print("______________________________________________________________________________________________________________")
#print(html)
#items = html['items']
result = requests.get(url, params=params, headers=headers).text

jsonData = json.loads(result)

#print(json.dumps(jsonData, ensure_ascii=False, indent=2))
#exit()



e = "(http(s)*|:|/)"

jsonData = json.loads(html)
items = jsonData['items']
Blogger = []
for item in items:
    # print ("title: " , item['title'])
    # print ("link: " , item['link'])
    # print ("bloggername: ", item['bloggername'])
    # print ("postdate: ", item['postdate'])
    bloggerID = re.sub(e, "", item['bloggerlink'])
    #print(bloggerID)
    #exit()
    Blogger.append([item['bloggerID'], item['bloggername'], item['bloggerlink']])
    #print(lst)
    exit()
#print(json.dumps(jsonData, ensure_ascii=False, indent=2))

def get_conn(db):
    return pymysql.connect(
        host='localhost',
        user='dooo',
        password='1234',
        port=3306,
        db=db,
        charset='utf8')

sql_truncate = "truncate table Blogger"
sql_insert = "insert into Blogger(bloggerID , bloggername, link) values(%s,%s,%s)"

conn = get_conn('dooodb')
with conn:
    cur = conn.cursor()
    cur.execute(sql_truncate)
    cur.executemany(sql_insert,Blogger)
    print("Affected RowCount is", cur.rowcount)



jsonData = json.loads(html)
items = jsonData['items']
BlogPost = []
for item in items:
    # print ("title: " , item['title'])
    # print ("link: " , item['link'])
    # print ("bloggername: ", item['bloggername'])
    # print ("postdate: ", item['postdate'])

    BlogPost.append([item['title'],  item['link'], item['bloggerID']])
    #print(lst)
    #exit()
#print(json.dumps(jsonData, ensure_ascii=False, indent=2))

def get_conn(db):
    return pymysql.connect(
        host='localhost',
        user='dooo',
        password='1234',
        port=3306,
        db=db,
        charset='utf8')

sql_truncate = "truncate table BlogPost"
sql_insert = "insert into BlogPost(title, link, bloggerID) values(%s,%s,%s)"

conn = get_conn('dooodb')
with conn:
    cur = conn.cursor()
    cur.execute(sql_truncate)
    cur.executemany(sql_insert,BlogPost)
    print("Affected RowCount is", cur.rowcount)

#re.sub("[http(s)*: \ /, "", link]")

# CREATE TABLE `Python` (
#   `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
#   `title` varchar(100) NOT NULL,
#   `link` varchar(100) NOT NULL,
#   `bloggername` varchar(100) NOT NULL,
#   `postdate` varchar(100) NOT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8;
