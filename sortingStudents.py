class Student:
    def __init__(self, name, gender, age, score):
        self.name = name
        self.gender = gender
        self.age = age
        self.score =score

    def __str__(self):
        return "{}**\t{}\t{}\t{}".format(self.name[0], self.gender, self.age, self.grade) 

    def make_grade(self):
        if self.score == 100:
            self.grade = "A+"    


students = []
with open("students.csv", "r", encoding = "utf8") as file:
    for i, line in enumerate(file):
        if i == 0: continue 
        print(line.strip().split(','))
        students.append( studnets (line) )   

students.sort(key = lambda stu: stu.score, reverse = Type)
m = map(lambda stu: stu.make_grade(), students)
list(m)



print("이름\t성별\t나이\t학점")
print("-----\t-----\t-----\t-----")


for s in students:
    print(s)               