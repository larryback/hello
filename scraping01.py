### 위키 문헌에 공개돼 있는 윤동주 작가의 작품 목록 가져오기

from bs4 import BeautifulSoup

import urllib.request as req



# 위키 윤동주 페이지를 받아와서 BeautifulSoup을 이용해 parsing한다.

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"

res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")



# div#mw-content-text 아래에 있는

# div.mw-parser-output 아래에 있는

# ul 태그 아래에 있는

# li 태그 아래에 있는

# a 태그를 모두 선택한다.

a_list = soup.select("div#mw-content-text > div.mw-parser-output > ul > li > a")



# 출력한다.

for a in a_list:

    name = a.string

    print("-", name)