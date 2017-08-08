

def calc_prod(lst):
	def f():
		ans = 1
		for i in lst:
			ans *= i
		return ans
	return f

f = calc_prod([1,2,3,4])
print (f())
