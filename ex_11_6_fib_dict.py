import pm

known = {0:0, 1:1}

def fibonacci(n):
  if n in known:
     return known[n]
  
  res = fibonacci(n-1) + fibonacci(n-2)
  known[n] = res
  return res

def fibonacci_classic(n):
 if n == 0:
   return 0
 elif n==1:
   return 1
 else:
   return fibonacci_classic(n-1) + fibonacci_classic(n-2)

z = pm.pm()

for n in range(30,37):
  print "  n = %d" % (n,)
  z.start()
  print fibonacci_classic(n)
  print z

  z.start()
  print fibonacci(n)
  print z

