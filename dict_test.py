import datetime
#import time


def has_letters(word, letters):
  for letter in word:
    if letter in letters:
      return True
  
  return False 

def is_palindrome(word):
 i=0
 j = len(word)-1
 while i<j:
   if word[i] != word[j]:
     return False
   i = i+1
   j = j-1
 return True

def is_reverse(word1, word2):
 if len(word1) != len(word2):
   return False
   i=0
   j = len(word2)
   while j > 0:
     if word1[i] != word2[j]:
       return False
       i = i+1
       j = j-1
 return True

cnt = 0
cnt_e = 0
cnt_p = 0

w = []
letters = 'e'


dt1 = datetime.datetime.now()
fin = open("113809of.fic")
for line in fin:
  word = line.strip()
  cnt = cnt + 1
  if has_letters(word,letters):
    cnt_e = cnt_e + 1
  

  l = len(word)
  lw = len(w)
  if lw < l:
    while lw < l:
      w.append(0)
      lw = lw + 1

  w[l-1]=w[l-1]+1
  #if l==20:
  #  print word

  if is_palindrome(word):
    cnt_p = cnt_p + 1
    print word 

fin.close()
#time.sleep(5)
dt2 = datetime.datetime.now()
dt = dt2 - dt1
print dt 

#pers = cnt_e * 100 / cnt 
#print "total words %d, words with %s %d, this is %d%%" % (cnt,letters,cnt_e,pers)
pers = cnt_p * 100 / cnt 
print "total words %d, palindroms %d, this is %d%%" % (cnt,cnt_p,pers)
print w
print [x*100/cnt for x in w]

cnt = 0
maxl = 0;
dt1 = datetime.datetime.now()
fin = open("113809of.fic")
for line in fin:
  word = line.strip()
  cnt = cnt + 1  

  l = len(word)
  if l> maxl:
    maxl = l

fin.close()
w = [0]*maxl
fin = open("113809of.fic")
for line in fin:
  word = line.strip()
  l = len(word)
  w[l-1]=w[l-1]+1

fin.close()
#time.sleep(5)
dt2 = datetime.datetime.now()
dt = dt2 - dt1
print dt 
print w
 
