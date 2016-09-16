
def _factorial(n):
  return reduce(lambda x,y: x*y, [1]+range(1,n+1))
  
def _simple(n)
  return reduce(lambda x,y: x and bool(n % y), range(2,n), True)

def factorial_list(l):
  #return map(lambda n: reduce(lambda x,y: x*y, [1]+range(1,n+1)),l)
  return map(_factorial, l)

def random_fill():
  return [random.randint(0,100) for x in [None]*6]
  #return map(lambda x: random.randint(0,100), [None] * 6)

def _min(l):
  return reduce(lambda x,y: y if x>y else x,l)

def _max(l):
  return reduce(lambda x,y: y if x<y else x,l)

def anti_vowel(s):
  return filter(lambda x: not x in 'aeiuoAEIUO', s)
  
  #return reduce(lambda x,y: x+y if not y in 'aeiuoAEIUO' else x+'' , s, '')
  
  #res = ''
  #z = s.lower()
  #for n in range(len(s)):
	#print s[n]
    #if not z[n] in 'aeiuo':
      #res = res + s[n]
          
  #return res
