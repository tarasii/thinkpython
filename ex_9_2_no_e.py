import mystr
import pm

l = mystr.file_to_list_classic("113809of.fic")

def words_no_letters(wocab, letters):
  res = []
  for x in wocab:
  if not mystr.has_letters(x, letters):
    res.append(x)
  return res

def words_no_letters_func(wocab, letters):
  return filter(lamda a: not mystr.has_letters(a, letters), wocab)

letters = "e"
  
z = pm.pm()
rl = words_no_letters(l, letters)
print z

cnt = len(l)
cnt_e = len(rl)
pers = cnt_e * 100 / cnt 
print "total words %d, words with no %s %d, this is %d%%" % (cnt,letters,cnt_e,pers)



z.start()
rl = words_no_letters_func(l,"e")
print z

cnt = len(l)
cnt_e = len(rl)
pers = cnt_e * 100 / cnt 
print "total words %d, words with no %s %d, this is %d%%" % (cnt,letters,cnt_e,pers)
