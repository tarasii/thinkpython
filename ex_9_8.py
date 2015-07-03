def is_palindrome(word):
  return word[::-1] == word
  #i = 0
  #j = len(word)-1
  #while i<j:
    #if word[i] != word[j]:
      #return False
    #i = i+1
    #j = j-1
  #return True

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

def funktional_check():   
   #generate list of numbers
   nm = ["%06d" % x for x in range(1000000)]

   #filtering 6 polinoms
   pl = filter(lambda x: is_palindrome(x), nm)

   #check loop
   for x in pl:
      tmp = int(x)
      if tmp > 4:
         pl1 = "%06d" % (tmp - 1)
         pl2 = "%06d" % (tmp - 2)
         pl3 = "%06d" % (tmp - 3)
         if is_palindrome(pl1[1:5]) and is_palindrome(pl2[1:6]) and is_palindrome(pl3[2:6]):
            print pl3, pl2, pl1, x 

 standart_check()
 funktional_check()
