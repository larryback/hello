import statistics
import re
import sys
from pprint import pprint

a ='''0067011990999991950051507004+68750+023550FM-12+038299999V0203301N00671220001CN9999999N9+00001+99999999999
0043011990999991945051512004+68750+023550FM-12+038299999V0203201N00671220001CN9999999N9+00225+99999999999
0043011990999991950051518004+68750+023550FM-12+038299999V0203201N00261220001CN9999999N9-00111+99999999999
0043012650999991949032412004+62300+010750FM-12+048599999V0202701N00461220001CN0500001N9+01117+99999999999
0043012650999991943032418004+62300+010750FM-12+048599999V0202701N00461220001CN0500001N9+00384+99999999999
0043012650999991945032412004+62300+010750FM-12+048599999V0202701N00461220001CN0500001N9+00167+99999999999
0043012650999991947032412004+62300+010750FM-12+048599999V0202701N00461220001CN0500001N9-00150+99999999999
0043012650999991949032412004+62300+010750FM-12+048599999V0202701N00461220001CN0500001N9+00117+99999999999
0043012650999991947032412004+62300+010750FM-12+048599999V0202701N00461220001CN0500001N9+00227+99999999999
0043012650999991945032412004+62300+010750FM-12+048599999V0202701N00461220001CN0500001N9+01116+99999999999
0043012650999991943032412004+62300+010750FM-12+048599999V0202701N00461220001CN0500001N9-00114+99999999999
0043012650999991943032412004+62300+010750FM-12+048599999V0202701N00461220001CN0500001N9+00191+99999999999
0043012650999991949032412004+62300+010750FM-12+048599999V0202701N00461220001CN0500001N9+00131+99999999999'''


lines = a.split('\n')
temp_idx = a.index('99999999999')
year_idx = a.index('099999') + len('099999')
select = '01459'
data = ''
temps = []
years = []
for line in lines:
    if line[(temp_idx - 2)] in select:
        year = line[year_idx: (year_idx+4)]
        temp = line[(temp_idx - 6):(temp_idx -2)]
        if line[(temp_idx-7)] == '+':
            temp = int(temp)    
        else : 
            temp = -int(temp)
            data = data + str(year) + '\t' +  str(temp) + ','
            
    print(data) 


#exit()

def fn1():
    ret = {}
    prekey = None
    for i in data:
        # key = i[0]
        # val = i[1]
        (key, val) = i
        if key != prekey:
            ret[key] = [val]
            prekey = key

        else:
            lst = ret[key]
            lst.append(val)

    pprint(ret)
    for y, l in ret.items():
        print(y, max(l))

#fn2()
fn1()




# def Reduce (data):
#     splt_data = data.split(',')[0:-1]
#     temp = []
#     year = []
#     res = []
#     year_temp = {}
#     result = []
#     for datum in splt_data :
#         splt_datum = datum.split('\t')
#         if splt_datum[0] not in year:
#             year.append(splt_datum[0])
#             temp.append([splt_datum[1]])
#         else :
#             b = year.index(splt_datum[0])
#             temp[b].append(splt_datum[1])

#     for i in temp:
#         res.append(sorted(i))

#     for i, j in enumerate(year):
#         year_temp[j]= res[i]

#     for x, y in year_temp.items():
#         print (x, max(y))




# print (Reduce(Map()))







