class Student:
    def_init_(self, name, score):
        self.name = name
        self.score = score

Students = [Student('유비', 90),Student('관우', 85),Student('장비', 95)]
for each in students:
    print(each.name, each.score)