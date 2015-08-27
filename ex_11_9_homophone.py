import mystr
import pm

def file_to_dict(fn):
  cnt = 0
  d = {}
  fin = open(fn)
  for line in fin:
    if line[0:2]=="##":
      continue

    x = line.split("  ")
    if len(x)<2:
      continue
    
    #print x
    word = x[0].strip().lower()

    #if word[-3:]=="(2)":
    #  d[word[:-3]].append(x[1])
    #else:
    #  d[word] = [x[1].strip()]

    d[word] = x[1].strip()

    #if len(d) == 100:
    #  break

    cnt += 1
    if cnt % 1000 == 0:
      print ".",

  print ""
  print ""
    
  return d

def list_to_dic(w):
  d = {}
  for x in w:
    d[x] = []
    
  return d

def check_word(wocab, word):
  word1 = word[1:]
  if word not in wocab:
    return None

  if word1 not in wocab:
    return None
    
  word2 = word[0]+word[2:]
  if word2 not in wocab:
    return None


  if wocab[word]==wocab[word1] and wocab[word]==wocab[word2] and word1<>word2:
    print ""
    print word, wocab[word], word1, wocab[word1], word2, wocab[word2]
  
  return None
  
def print_pairs(d):
  for x in d:
    if len(d[x])>0:
      print x, d[x]

letter_a = ord("a")
letter_z = ord("z")
letter_number = letter_z - letter_a + 1
  
zz = pm.pm()
l = mystr.file_to_list_classic("113809of.fic")
d = file_to_dict("c06d.txt")
#d = list_to_dic(l)
print zz

cnt = 0
db = {}
for x in l:
  check_word(d,x)
  cnt += 1
  if cnt % 1000 == 0:
    print ".",

print ""



#print_pairs(d)

#zz.start()
#find_rotate_pairs(l, d)

#print zz

#zz.start()
#print_pairs(d)
#print zz
