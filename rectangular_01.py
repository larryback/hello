class Quadrangle:
    pass



r.input("Input(usage: length, width)>> ")

p.input("Input(usage: base, height)>> ")



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

r.input("Input(usage: length, width)>> ")

p.input("Input(usage: base, height)>> ")




    
       




#직사각형 = rectangle
# 평행사변형 parallelogram

