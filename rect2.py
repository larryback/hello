class Casting:
    def to_int(s):
        if type(s) == str:
            return int(s.strip())
        else:
            return s

class 사각형:
    name = "사각형"
    def __init__(self):
        print("사각형 created")

    def input_data(self):
        datum = input(self.msg)  # 5, 3
        data = datum.split(',')  # ['5', '3']
        x, y = Casting.to_int(data[0]), Casting.to_int(data[1])
        self.__새넓이(x, y)

    def __새넓이(self, x, y):
        r = x * y
        print("{}의 넓이는 {}입니다".format(self.name, r))

class 직사각형(사각형):
    name = "직사각형"
    msg = "가로와 세로는?? (usage: 가로,세로)"
    
class 평행사변형(사각형):
    name = "평행사변형"
    msg = "밑변와 높이는?? (usage: 밑변, 높이)"









all_rects = [직사각형(), 평행사변형()]

while True:
    print()
    rect_type = input("사각형의 종류는?\n 1) 직사각형\n 2)평행사변형\n (quit:q) >> ")
    if (rect_type == 'q'):
        break

    rect_index = Casting.to_int(rect_type) - 1
    rect = all_rects[rect_index]
    x, y = input_data()