import json

dic = {}

# html 파싱 데이터
dic0 = {"songno": 1, "name": "aaa", "like": 0}
dic1 = {"songno": 2, "name": "bbb", "like": 0}
dic0 = {"id": 1, "name": "aaa", "like": 0}
dic1 = {"id": 2, "name": "bbb", "like": 0}

# dic에 dic0과 dic1을 키값 songno로 추가하기
dic[dic0['songno']] = dic0
dic[dic1['songno']] = dic1
dic[dic0['name']] = dic0
dic[dic1['name']] = dic1

print(dic)
print("-------------------------------------")


# 찾기
songno = dic1['songno']
bbbJson = dic[songno]
bbbJson = dic['bbb']

# 수정 및 추가하기
bbbJson['like'] = 1
bbbJson.update({'others': 'pppppppp'})

print(dic[songno])
print(dic)

j = json.loads(dic)
print(dic['bbb'])
print(dic) 