def square_generator(n):
  i = 0
  while i<n:
    yield i*i
    i+=1

def fib_generator(n):
  a, b = 0, 1
  i = 0
  while i<=n:
    yield a
    a, b = b, a+b
    i+=1

def fib_negative_generator(n):
  a, b = 0, 1
  i = 0
  while i<=n:
    yield a
    a, b = b, a-b
    i+=1

def factorial_generator(n):
  a = 1
  i = 1
  while i<=n:
    yield a
    a*=i
    i+=1

def myrange(start,end,step=1):
  i = start
  while i<end:
    yield i
    i+=step


print range(10)
print [x for x in myrange(0,10)]

print [x*x for x in myrange(0,10)]
print [x for x in square_generator(10)]

print [x for x in fib_generator(10)]
print [x for x in fib_negative_generator(10)]
print [x for x in factorial_generator(10)]

