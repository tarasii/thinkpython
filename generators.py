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
    a, b, i = b, a+b, i+1

def fib_negative_generator(n):
  a, b, i = 0, 1, 0
  while i<=n:
    yield a
    a, b, i = b, a-b, i+1

def factorial_generator(n):
  a, i = 1, 1
  while i<=n:
    yield a
    a, i = a*i, i+1

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

