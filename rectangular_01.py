cmd = input("Input(usage: base, length, width)>> ")
print(cmd)
cmds = cmd.split(",")
print("{},{},{}".format(cmds[0], cmds[1], cmds[2]))




class Quadrangle:
    def __init__(self, base, height, width):
        self.base = 0
        self.height = 0
        self.width = 0

 

class Rectangle(Quadrangle):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        r_area = length * width 
        print(r_area)
       

        r = Rectangle(length, width)

class Parallelogram(Quadrangle):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        p_area = base * height
        print(p_area)

        p = Parallelogram (base, height)

class Square(Quadrangle):
    def __init__(self, length):
        self.length = length
        s_area = length * length
        print(s_area)


        s = Square (length, length)






    
       




# 직사각형 = rectangle
# 평행사변형= parallelogram
#  정사각형 = square 
