import pm

def sumall(*args):
  res = 0
  for x in args:
    res += x

  return res

print sumall(1,5,6,55)
