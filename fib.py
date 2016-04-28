import pm
c = 0;


def fib(n):
  global c 
  c +=1

  if n == 0:
    return 0
  elif n == 1:
    return 1
  elif n == -1:
    return 1

  if n < -1:
    return fib(n+2)-fib(n+1)
  else:
    return fib(n-2)+fib(n-1)


def fib_range(n):
  a,b = 0,1
  if n>0:
    for i in range(n):
      a,b = b,a+b
  else:
    for i in range(0, n, -1):
      a,b = b,a-b

  return a

#endles generator
def fib_generator():
    a,b = 0,1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


n = 10
pm = pm.pm()
print n, fib(n), c
print pm
pm.start()
print n, fib_range(n)
print pm
pm.start()
fb = fib_generator()
for x in range(n):
  fb.next()
print n, fb.next()
print pm


for x in range(10):
   c = 0
   print x, fib(x), c

res = [fib(x) for x in range(-10,11)]
print res
res = [fib_range(x) for x in range(-10,11)]
print res
