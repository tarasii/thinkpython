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
    if t > z:
      t = t - z + a - 1
    elif t < a:
      t = t + z - a + 1
    #rint x, ord(x), t

    res += chr(t)
    
  return res

a = ord("a")
z = ord("z")
y = z - a + 1
  
zz = pm.pm()
l = mystr.file_to_list_classic("113809of.fic")
#d = file_to_dict_classic("113809of.fic")
print zz

d = {}
for x in l:
  d[x] = []

zz.start()
for x in l:
  for n in range(1, y):
    r = rotate_word(x, n)
    if r in d:
      print x, r  
      d[x].append(r)

print zz

zz.start()
for x in l:
  if len(d[x])>0:
    print x, d[x]

print zz
