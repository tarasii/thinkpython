#generate list of numbers
nm = ["%06d" % x for x in range(1000000)]

#filtering 6 polinoms
pl = filter(lambda x: is_palindrome(x), nm)

#
for x in pl:
   tmp = int(x)
   pl1 = "%06d" % (tmp - 1)
   pl2 = "%06d" % (tmp - 2)
   pl3 = "%06d" % (tmp - 3)
   if tmp > 4:
      if is_palindrome(pl1[1:5]) and is_palindrome(pl2[1:6]) and is_palindrome(pl3[2:6]):
         print pl3, pl2, pl1, x 
