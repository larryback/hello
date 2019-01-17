from bs4 import BeautifulSoup
from pprint import pprint
import json


html = '''
<!doctype html>
<html lang="ko">
  <head>
    <meta charset="utf-8">
    <title>HTML</title>
    <style>
      table {
        width: 100%;
      }
      table, th, td {
        border: 1px solid #bcbcbc;
      }
    </style>
  </head>

<table>
    <tr>
        <th>회사</th>
        <th>A사</th>
        <th>B사</th>
        <th>C사</th>
        <td rowspan="2">Dolor</td>
    </tr>
    <tr>
        <th>주소</th>
        <td>서울</td>
        <td>강원도</td>
        <td>부산</td>
        <td rowspan="2">Dolor</td>
    </tr>
    <tr>
        <th>직원수</th>
        <td>30명</td>
        <td>55명</td>
        <td>200명</td>
        <td rowspan="2">Dolor</td>
    </tr>
    <tr>
        <th>전화번호</th>
        <td>02-2345-2323</td>
        <td>033-223-2323</td>
        <td>051-121-1212</td>
        <td rowspan="2">Dolor</td>
    </tr>
    <tr>
        <th>대표메일</th>
        <td>a@a.com</td>
        <td>b@b.com</td>
        <td>c@c.com</td>
        <td rowspan="2">Dolor</td>
    </tr>
</table>
'''

print(html)
soup = BeautifulSoup(html, "html.parser")

data={
 "A사":[
         {"주소":"서울"},
         {"직원수":"30명"},
         {"전화번호":"02-2345-2323"},
         {"email":"a@a.com"}
        ],
"B사":[
         {"주소":"강원도"},
         {"직원수":"55명"},
         {"전화번호":"033-223-2323"},
         {"email":"b@b.com"}
        ],
"C사":[
        {"주소":"부산"},
        {"직원수":"200명"},
        {"전화번호":"051-121-1212"},
        {"email":"c@c.com"}
        ]  

}

# JSON 인코딩
jsonString = json.dumps(data)
 
# 문자열 출력
print(jsonString)
print(type(jsonString))   # class str

jsonString = json.dumps(data, indent=4)
print(jsonString)


#exit()

# JSON 디코딩
dict = json.loads(jsonString)

# Dictionary 데이타 체크
print(dict['A사'])




#with open('./data.json') as data_file:    
#    data = json.load(data_file)

#pprint(data)

