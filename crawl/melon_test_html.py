import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import csv, codecs
import re
import pymysql

html1 = """
<dl class="info_02 clfix">
        <dt>국적</dt><dd>대한민국</dd>
        <dt>활동유형</dt><dd>여성, 솔로</dd>
        <dt>활동년대</dt><dd>2010</dd>

        <dt>활동장르</dt>
        <dd>Dance, Ballad, Drama</dd>

        <dt>데뷔</dt>
        <dd class="debut_song">
            <span class="ellipsis">2016.05.05<span class="bar"></span></span>
        </dd>

        <dt>생일</dt>
        <dd>1996.02.09</dd>
    </dl>
"""    

html2 = """
<dl class="info_02 clfix">
        <dt>국적</dt>
        <dd>대한민국</dd>

        <dt>활동유형</dt>
        <dd>여성, 솔로</dd>

        <dt>활동년대</dt>
        <dd>2010</dd>
        
        <dt>활동장르</dt>
        <dd>Dance, Ballad, Drama</dd>
    
        <dt>데뷔</dt>
        <dd class="debut_song">
            <span class="ellipsis">
                2016.05.05
                <span class="bar">
                    TTT
                </span>
            </span>
        </dd>
        
        <dt>생일</dt>
        <dd>1996.02.09</dd>
    </dl>
    """

soup = BeautifulSoup(html2, 'html.parser')

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

print(vals)