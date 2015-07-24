import mystr
import pm

l = mystr.file_to_list_classic("113809of.fic")

def len_more(wocab, ln):
  res = []
  for x in wocab:
    if len(x)>ln:
      res.append(x)

  return res

def len_more_funk(wocab, ln):
  return filter(lambda a: len(a)>ln, wocab)
  
z = pm.pm()
rl = len_more(l, 20)
print z

cnt = len(l)
cnt_e = len(rl)
pers = cnt_e * 100 / cnt 
print "total words %d, %d words longer 20, this is %d%%" % (cnt,cnt_e,pers)
print rl


z.start()
rl = len_more_funk(l, 20)
print z

cnt = len(l)
cnt_e = len(rl)
pers = cnt_e * 100 / cnt 
print "total words %d, %d words longer 20, this is %d%%" % (cnt,cnt_e,pers)
print rl
print map(lambda a: len(a),rl)
