class A:
	# class attribu
	a = 9
	# method (constructor)
	def __init__(self, a, b):
		# instance attributes (properties)
		self.a = a
		self.b = b

	def __str__(self):
		return f'a: {self.a}\nb: {self.b}'


obj1 = A()
obj2 = A(3,4)


print(obj1.a)
print(A.a)
print(obj2.a)


