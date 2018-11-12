class TestClass:
    name = "Test"

    def get_name(self):
        return self.name


class Child(TestClass):
    def get_name(self):
        return "Child Name" + self.name

test = TestClass() 
print("111111>>", test.get_name())   
