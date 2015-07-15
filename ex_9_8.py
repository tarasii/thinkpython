def is_palindrome_classic(word):
  i = 0
  j = len(word)-1
  while i<j:
    if word[i] != word[j]:
      return False
    i = i+1
    j = j-1
  return True

def is_palindrome(word):
  return word[::-1] == word

def check(i):
    pl = "%06d" % (i)
    pl1 = "%06d" % (i+1)
    pl2 = "%06d" % (i+2)
    pl3 = "%06d" % (i+3)
    return (is_palindrome(pl[2:6])   and
            is_palindrome(pl1[1:6]) and
            is_palindrome(pl2[1:5]) and
            is_palindrome(pl3))

def classic_check():
   i = 0
   while i <= 999996:
      if check(i):
        print i
      i = i + 1

def functional_check():   
   nm = ["%06d" % x for x in range(1000000)]
   pl = filter(lambda x: check(x), nm)
   print pl
   

standart_check()
functional_check()
