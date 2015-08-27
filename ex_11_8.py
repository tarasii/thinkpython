import mystr
import pm

def file_to_dict_classic(fn):
  t = {}
  fin = open(fn)
  for line in fin:
    word = line.strip()
    t[word] = []

  return t

def rotate_word(word, n):
  res = ""
  for x in word.lower():
    t = ord(x) + n
    if t > letter_z:
      t = t - letter_z + letter_a - 1
    elif t < letter_a:
      t = t + letter_z - letter_a + 1
    #rint x, ord(x), t

    res += chr(t)
    
  return res

def list_to_dic(w):
  d = {}
  for x in w:
    d[x] = []
    
  return d
  
def find_rotate_pairs(l, d):
  for x in l:
    for n in range(1, y):
      r = rotate_word(x, n)
      if r in d:
        print x, r  
        d[x].append(r)
        
  return none
  
def print_pairs(d):
  for x in l:
    if len(d[x])>0:
      print x, d[x]

letter_a = ord("a")
letter_z = ord("z")
y = letter_z - letter_a + 1
  
zz = pm.pm()
l = mystr.file_to_list_classic("113809of.fic")
#d = file_to_dict_classic("113809of.fic")
d = list_to_dic(l)
print zz


zz.start()
find_rotate_pairs(l, d)

print zz

zz.start()
print_pairs(d)
print zz
