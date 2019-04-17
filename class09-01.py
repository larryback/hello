# 클래스를 선언합니다.
class Student:

     def __init__(self, name, korean, math, english, science):

        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

     def get_sum(self):
        return self.korean + self.math + self.english + self.science
        
     def get_average(self):
        return self.get_sum() / 4
        # 생략

     def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average())

# 학생 리스트를 선언합니다.

students = [Student("윤인성", 87, 98, 88, 95), Student("서준서", 45, 52, 72, 78)]            

# 출력합니다.

print("이름", "총점", "평균", sep = "\t")
for student in students:
    print(str(student))    