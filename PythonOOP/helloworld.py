class HelloWorld():
	def __init__(self):
		x = 0
		while x < 10:
			print(x)
			x += 1
	def firstprogram(self):
		print("HelloWorld")

	def larger(self, x, y):
		if (x > y):
			return x
		return y



a = HelloWorld()
print(a.firstprogram())
print(a.larger(2,3))
