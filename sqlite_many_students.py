import pymysql
import random

fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")

def make_names():
    sung = random.choice(fam_names)
    name = "".join(random.sample(first_names, 2))
    return (sung+name, )


data =[]
for i in range(0, 10):
    data.append(make_names())

print(data)

a = '010'
b = list('0123456789')
c = list('0123456789')

def make_phone_number():
    second = "".join(random.sample(b, 4))
    third = "".join(random.sample(c, 4))
    phone_number=a+second+third)
    
    return phone_number


tel = []
for i in range(0, 10):
    tel.append(make_phone_number())    


print(tel)