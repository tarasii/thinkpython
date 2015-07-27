import mystr
import pm


def is_abecederian(word):
  previous = word[0]
  for c in word:
    if c < previous:
      return False
    previous = c

  return True

def check_abecederian(wocab):
  res = []
  for x in wocab:
    if is_abecederian(x):
      res.append(x)
  return res 
  
z = pm.pm()
l = mystr.file_to_list_classic("113809of.fic")
print z


z.start()
rl = check_abecederian(l)
print z

print len(rl)
print rl
