# 클래스를 선언합니다.
class Student:
    def __init__(self, name, korean, math, english, science):
        # 인스턴스 변수 초기화
        self.name = name
        self.korean = korean
        self.math = math
    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science
    # 나머지 메서드는 보기 힘듦으로 생략할게요
    def __eq__(self, value): 
        if not isinstance(value, Student):
            raise TypeError("Student 클래스의 인스턴스만 비교할 수 있습니다")
        return self.get_sum() == value.get_sum()

# 학생을 선언합니다.
student_a = Student("윤인성", 87, 98, 88, 95)
# 비교합니다.
student_a == 10