class Account:
	def __init__(self, balance) -> None:
		self.__balance = balance

	@property
	def balance(self):
		print('balance getter is called')
		return self.__balance

	# setter
	@balance.setter
	def balance(self, x):
		print('balance setter is called')
		self.__balance = x


a1 = Account(100)

# a1.balance()
print( a1.balance )

a1.balance = -200