import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import csv, codecs
import re
import pymysql

html = '''
    <dl>
        <dt>국적</dt>
        <dd>대한민국</dd>

        <dt>활동장르</dt>
        <dd>Dance, Ballad, Drama</dd>
    
        <dt>데뷔</dt>
        <dd class="debut_song">
            <span class="ellipsis">
                2016.05.05
                <span class="bar">
                    TTT
                </span>
                <a href="#">TTTTTTTTTTTTT</a>
            </span>
        </dd>
        
        <dt>수상이력</dt>
        <dd class="awarded">
            <span class="ellipsis">
                2018 하이원 서울가요대상
                <span class="bar">|</span>본상
            </span>
        </dd>
    </dl>
'''

soup = BeautifulSoup(html, 'html.parser')
col_names = {'국적':'nation', '활동장르':'genre', '데뷔':'debut', '수상이력':'award' }

dl = soup.find('dl')
dts = []
dds = []
for d in dl:
    if not d.name: continue

    if d.name == 'dt':
        dts.append(col_names[d.text])
    else:
        span = d.select_one('span')
        if span != None:
            print("ssssssssssssS>>", span.text)
            dds.append(span.next.strip())
        else:
            dds.append(d.text)

vals = {}
for i in range(len(dts)):
    vals[dts[i]] =  dds[i]

#print(vals)

#exit()

print("Insert into Singer({0}, {1}, {2}, {3}) values ({4}, {5}, {6}, {7}) ;".format('nation','genre','debut', 'award', '국적', '활동장르', '데뷔','수상이력' ))