class Dog:
	def __init__(self):
		self.name = "Dog"
		print("Dog was Born")

	def speak(self):
		print("YELP!", self.name)
def wag(self):
		print("Dog's wag tail")
def __del__(self):
		print("destroy!!")



class Puppy(Dog):
	def __init__(self):
		self.name = "Puppy"
		print("Puppy was Born")
	def wag(self):
		print("Puppy's wag tail")
      
d = Dog('puddle')  
p = Puppy()    
d.speak() 
p.speak()


