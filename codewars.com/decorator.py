import time

def performance(f):
	def wrapper(args):
		start=time.ctime()
		print('call ' + f.__name__ + '() in:' + start)
		return f(args)
	return wrapper

@performance
def factorial(n):
	return reduce(lambda x,y: x*y, range(1, n+1))

print(factorial(4))
