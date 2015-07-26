import pm
import mystr

def filter_palindroms(wocab):
  res = []
  for x in wocab:
    if mystr.is_palindrome(x):
      res.append(x)

  return res

def filter_palindroms_func(wocab):
  return filter(lambda a: mystr.is_palindrome(a), wocab)

def file_to_list_dump():
  t = []
  fin = open("113809of.fic")
  for line in fin:
    word = line.strip()
    t = t + [word]

  fin.close()
  return t


p = pm.pm()
l = mystr.file_to_list_classic("113809of.fic")
print p

p.start()
rl = filter_palindroms(l)
print p

cnt = len(l)
cnt_e = len(rl)
pers = cnt_e * 100 / cnt 
print "total words %d, palindroms %d, this is %d%%" % (cnt,cnt_e,pers)


p.start()
rl = filter_palindroms_func(l)
print p

cnt = len(l)
cnt_e = len(rl)
pers = cnt_e * 100 / cnt 
print "total words %d, palindroms %d, this is %d%%" % (cnt,cnt_e,pers)




