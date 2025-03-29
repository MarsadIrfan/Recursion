
def fibonacci(nthNumber):
	a, b = 1, 1
	for i in range(nthNumber):
		a, b = b, a+b
		print('a=%s, b=%s' % (a, b))
	return a

print(fibonacci(10))
