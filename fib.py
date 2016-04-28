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


def fib_dict(n, _cache={}):

  if n in _cache:
    return _cache[n]

  if n == 0:
    res = 0
    _cache.setdefault(n, res)  
    return res
  elif n == 1:
    res = 1
    _cache.setdefault(n, res)
    return res
  elif n == -1:
    res = 1
    _cache.setdefault(n, res)
    return res

  if n < -1:
    res = fib_dict(n+2, _cache) - fib_dict(n+1, _cache)
    _cache.setdefault(n, res)
    return res
  else:
    res = fib_dict(n-2, _cache) + fib_dict(n-1, _cache)
    _cache.setdefault(n, res)
    return res


#good to generate lists
def memoize(fn, arg):
  memo = {}
  if arg not in memo:
    memo[arg] = fn(arg)
    return memo[arg]


def PM(fn):
  import pm
  def wrapped(*arg):
    z = pm.pm()
    res = fn(*arg)
    print z
    return res

  return wrapped


class Memoize:
  def __init__(self, fn):
    self.fn = fn
    self.memo = {}
  def __call__(self, arg):
    if arg not in self.memo:
      self.memo[arg] = self.fn(arg)
      return self.memo[arg]

@PM
@Memoize
def fib_memoize_range(n):
  a,b = 0,1
  if n>0:
    for i in range(n):
      a,b = b,a+b
  else:
    for i in range(0, n, -1):
      a,b = b,a-b

  return a

n = 15
pm = pm.pm()
print n, fib(n), c
print pm, "recursion"

print 
pm.start()
print n, fib_range(n)
print pm, "range"

print 
pm.start()
fb = fib_generator()
for x in range(n):
  fb.next()
print n, fb.next()
print pm, "generator"

print 
pm.start()
print n, fib_dict(n)
print pm, "dict"

print 
pm.start()
print n, memoize(fib, n)
print pm, "memoize recursion"

print
pm.start()
print n, memoize(fib_dict, n)
print pm, "memoize with dict"

print
pm.start()
print n, memoize(fib_range, n)
print pm, "memoize with range"

print
print "memoize decorator with range"
print n, fib_memoize_range(n)
 

#for x in range(10):
#   c = 0
#   print x, fib(x), c

#res = [fib(x) for x in range(-10,11)]
#print res
res = [fib_range(x) for x in range(-10,11)]
print res
