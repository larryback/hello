import random
from pprint import pprint
import json
from bs4 import BeautifulSoup
import numpy

data = {
    "A" : [
        [9, -9, -4,  3,  6],
        [7, -3, -8,  4,  4],
        [7, -9,  1, -2,  8],
        [5, -3, -4, -9, -8],
        [8,  5, -5,  4,  6]
    ],

    "B" : [
        [ 2, -7,  2, -2,  0],
        [ 1,  8,  2,  2, -2],
        [ 6, -2,  5, -2,  5],
        [-4,  9, -5, -9, -7],
        [ 8,  0, -9,  2, -7]
    ],

    "C" : [
        [-9,  5, -1,  9,  4],
        [ 3, -4, -6, -3,  3],
        [ 6,  6,  7, -3, -6],
        [-8,  9,  6, -1, -2],
        [-10, 2, -8, -4,  9]
    ]
}

pprint(data)

# 대각선의 합이 작은 것은?

# JSON 인코딩
jsonString = json.dumps(data)
 
#print("=====================================================================") 
# 문자열 출력
#print(jsonString)
#print(type(jsonString))   # class str

#list =data
i = 0
list = [[9, -9, -4,  3,  6],
        [7, -3, -8,  4,  4],
        [7, -9,  1, -2,  8],
        [5, -3, -4, -9, -8],
        [8,  5, -5,  4,  6]],

for l in list:

    sum([l[i] + l[-i-1]) 