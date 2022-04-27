class A:
  def foo(self):
    x = 5
    self.x = 5



  def bar(self):
    # print(x**2)
    print(self.x**2)

a = A()
a.foo()
a.bar()