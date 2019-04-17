#!/usr/bin/env python3

import sys
import urllib.request as req
import urllib.parse as parse

if len(sys.argv) <= 1:
    print('Error!!')
    exit()

regionNumber = sys.argv[1]
API = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
params = {
    "stdId": regionNumber
}

url = API + "?" + parse.urlencode(params)
print("url>>", url)

content = req.urlopen(url).read()
xml = content.decode('utf-8')

print(xml)