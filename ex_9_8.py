import mystr

def check(i):
    pl = "%06d" % (i)
    pl1 = "%06d" % (i+1)
    pl2 = "%06d" % (i+2)
    pl3 = "%06d" % (i+3)
    return (mystr.is_palindrome(pl[2:6])   and
            mystr.is_palindrome(pl1[1:6]) and
            mystr.is_palindrome(pl2[1:5]) and
            mystr.is_palindrome(pl3))

def check_classic():
   i = 0
   while i <= 999996:
      if check(i):
        print i
      i = i + 1

def check_func():   
   nm = [x for x in range(999997)]
   pl = filter(lambda x: check(x), nm)
   print pl

check_classic()
check_func()
