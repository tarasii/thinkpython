import mystr
import pm
import collections

l = mystr.file_to_list_classic("113809of.fic")

def len_statistics(wocab):
  maxl = 0;
  for word in wocab:
    l = len(word)
    if l > maxl:
      maxl = l
  
  print maxl
  
  w = [0] * maxl
  for line in wocab:
    word = line.strip()
    l = len(word)
    w[l-1] += 1

  return w

def len_statistics_2(wocab):
  w = []
  for line in wocab:
    word = line.strip()
    l = len(word)
    
    lw = len(w)
    if lw < l:
      while lw < l:
        w.append(0)
        lw = lw + 1

    w[l-1] += 1

  return w


def len_statistics_func(wocab):
  return collections.Counter(map(lambda a: len(a), wocab))
  
z = pm.pm()
rl = len_statistics(l)
print z
print rl

rl = len_statistics_2(l)
print z
print rl

z.start()
rl = len_statistics_func(l)
print z
print rl
