# 클래스를 선언합니다.
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science
    def get_average(self):
        return self.get_sum() / 4
    def to_string(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())
    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average())
    def __eq__(self, other): 
        return self.get_sum() == other.get_sum()
    def __ne__(self, other): 
        return self.get_sum() != other.get_sum()
    def __gt__(self, other):
        return self.get_sum() > other.get_sum()
    def __ge__(self, other):
        return self.get_sum() >= other.get_sum()
    def __lt__(self, other):
        return self.get_sum() < other.get_sum()
    def __le____(self, other):
        return self.get_sum() <= other.get_sum()

# 학생을 선언합니다.
student_a = Student("윤인성", 87, 98, 88, 95)
student_b = Student("연하진", 92, 98, 96, 98)

# 출력합니다.
print("student_a == student_b = ", student_a == student_b)
print("student_a != student_b = ", student_a != student_b)
print("student_a >  student_b = ", student_a >  student_b)
print("student_a >= student_b = ", student_a >= student_b)
print("student_a <  student_b = ", student_a <  student_b)
print("student_a <= student_b = ", student_a <= student_b)