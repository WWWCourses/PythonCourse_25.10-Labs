def foo(*x,**y):
	print(x)
	print(y)

args = (5,6)
kw = {'c':7,'d':8}

foo(*args, **kw)
# foo(5,6,c=7,d=8)