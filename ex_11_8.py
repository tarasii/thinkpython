import mystr
import pm

def file_to_dict_classic(fn):
  t = {}
  fin = open(fn)
  for line in fin:
    word = line.strip()
    t[word] = []

  return t

def rotate_letter(letter, n):
  x = ord(letter) + n
  if x > letter_z:
    x = x - letter_number
  elif x < letter_a:
    x = x + letter_number
    
  return chr(x)

def rotate_word(word, n):
  res = ""
  for letter in word.lower():
    res += rotate_letter(letter, n)
    
  return res

def list_to_dic(w):
  d = {}
  for x in w:
    d[x] = []
    
  return d
  
def rotate_pairs(d, x):
  for n in range(1, letter_number):
    r = rotate_word(x, n)
    if r in d:
      #print x, r  
      d[x].append(r)
        
  return None
  
def print_pairs(d):
  for x in l:
    if len(d[x])>0:
      print x, d[x]

letter_a = ord("a")
letter_z = ord("z")
letter_number = letter_z - letter_a + 1
  
zz = pm.pm()
l = mystr.file_to_list_classic("113809of.fic")
#d = file_to_dict_classic("113809of.fic")
d = list_to_dic(l)
print zz


zz.start()
cnt = 0
for x in l:
  rotate_pairs(d, x)

  cnt += 1
  if cnt % 1000 == 0:
    print ".",

print ""

print zz

zz.start()
print_pairs(d)
print zz
