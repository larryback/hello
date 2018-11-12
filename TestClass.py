class TestClass:
    name = "Test"

    def __init__(self):
        print("TTTTTTTTTTTT")
    
    def static_method():
        print("STATIC")
    @property
    def full_name(self):
        return self.name + "FFFFF"   
    
    def get_name(self):
        print("000000000000")
        return self.name

    def area(self, x, y):
        return x * y

class Child(TestClass):
    def __init__(self):
        super().__init__()
        print("my init!!!")

    def get_name(self):
        t = super().get_name()
        return "Child Name" + self.name

    def area(self, x, y):
        t = super().area(x, y)
        return t / 2 

test = TestClass()
child = Child()
print("FFFFFFF>>", test.full_name)

cmd = input("Input the function name>> ")

getattr(test, "get name")
getattr(TestClass, "static.method")()

# print("11111>>", child.get_name())

# c = callable(test.get_name)
# print("ccccccccccc>>", c)

test = TestClass() 
print("111111>>", test.get_name())   
