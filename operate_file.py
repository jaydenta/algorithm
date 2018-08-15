import time
def compare_add():
	def add(l):
		x = 0
		for i in l:
			x = x + i 
		return x

	start = time.time()
	x = 1000000
	print('Sum of 0 to {}'.format(x) + ' using add function is {}'.format(add(range(x))))
	end = time.time()
	print('add function takes {}'.format(end - start) + ' seconds to finish')

	def builtin_add(l):
		lSum = sum(l)
		#print(lSum)
		return lSum

	start = time.time()
	x = 1000000
	print('Sum of 0 to {}'.format(x) + ' using builtin_add is{}'.format(builtin_add(range(x))))
	end = time.time()
	print('builtin_add takes {}'.format(end - start) + ' seconds to finish')

def sum_element_squares(l):
	x = 0
	for i in l:
		x = x + ((i)**2)
	return x

def factorial(l):
	x = 1
	for i in l:
		x  = x * i
	return x