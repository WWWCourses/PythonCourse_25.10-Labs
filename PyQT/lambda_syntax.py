def caller(f,x,y):
	print(f)
	f(x,y)

def foo(x,y):
	print(x,y)


caller( foo, 3,4 )
caller( lambda x,y : print(x,y), 3,4 )

