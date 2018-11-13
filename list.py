int_numbers = range(-5, 6)
print(list(int_numbers))
negatives = filter(lambda x: x < 0, int_numbers)
print(list(negatives))
def fn(x):
	return x < 0
int_numbers = range(-5, 6)

double_numbers = map( make_double, numbers )
print( list(double_numbers) )