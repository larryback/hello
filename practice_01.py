# Non self argument
class Dog:
    def m1(self):
        print("m1")

    def speak(self):
	    print("YELP!", self.name)

    def m2():
        print("m2")

dog = Dog()

Dog.m2()

class Puppy(Dog):
	def __init__(self):
		self.name = "Puppy"
		print("Puppy was Born")
def wag(self):
		print("Puppy's wag tail")

def tto():
		print("Ttooooooooooo0000000000")


puppy = Puppy()

puppy.speak()

print("Name is", puppy.name)

print("isDog", isinstance(puppy, Dog))

print(wag(puppy))

Puppy.tto()