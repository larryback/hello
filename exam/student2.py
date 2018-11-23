from functools import reduce
from Student import Student
# import Student

g_grades = ['A', 'B', 'C', 'D', 'F']
g_grades.reverse()

students = []
with open('students.csv', 'r', encoding='utf8') as file:
    for i, line in enumerate(file):
        if i == 0: continue
        students.append( Student(line) )

students.sort(key = lambda stu: stu.score, reverse = True)
m = map(lambda stu: stu.make_grade(), students)
list(m)



print("이름\t성별\t나이\t학점\t주소")
print("----\t----\t----\t----\t----")
for s in students:
    print(s)

