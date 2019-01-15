dic = {}

# html 파싱 데이터
dic0 = {"songno": 1, "name": "aaa", "like": 0}
dic1 = {"songno": 2, "name": "bbb", "like": 0}

# dic에 dic0과 dic1을 키값 songno로 추가하기
dic[dic0['songno']] = dic0
dic[dic1['songno']] = dic1

print(dic)
print("-------------------------------------")


# 찾기
songno = dic1['songno']
bbbJson = dic[songno]

# 수정 및 추가하기
bbbJson['like'] = 1
bbbJson.update({'others': 'pppppppp'})

print(dic[songno])
print(dic)

# 찾기
bbbJson = dic['bbb']

# 못찾을 경우 (키 존재여부 체크하기)
if (dic.get('ccc')):
    bbbJson2 = dic['ccc']

# 수정 및 추가하기
bbbJson['like'] = 1
bbbJson.update({'others': 'pppppppp'})