class A:
	# class attribute
	id = 1

	def __init__(self, id) -> None:
		# instance attribute
		self.id = id
		# do somethin
		A.read_config()

	# instance method
	def get_id(self):
		print(self.id)

	# class method:
	def read_config():
		print('config readed')
		print(A.id)


a = A(9)
# call instance method:
a.get_id()
# call class method:
A.read_config()
