import pm
import mystr
import random

def sort_by_length(words):
  t = []
  for word in words:
    t.append((len(word), word))

  t.sort(reverse=True)
  res = []
  for length, word in t:
    res.append(word)

  return res


#tl = [(1,4,7),(2,3)]
#print tl
#tl[-1]= tl[-1]+(6,)
#print tl


z = pm.pm()
l = mystr.file_to_list_classic("113809of.fic")
print z


t = []
for word in l:
  t.append((len(word), word))

print z

t.sort(reverse=True)
print z

#res = []
#for length, word in t:
#  res.append(word)
#print z

curl = 0
tws = []
for tw in t:
  if curl <> tw[0]:
    tws.append([tw[1]])
    curl = tw[0]
  else:
    tws[-1].append(tw[1])
print z

print tws[:3]

res = []
for tw in tws:
  #for w in tw:
  while len(tw)>0:
    i = random.randint(0,len(tw)-1)
    res.append(tw[i])
    del (tw[i])
    #tw = tw[:i]+tw[i:]

print z


print res[:100]
#print sort_by_length(l)
