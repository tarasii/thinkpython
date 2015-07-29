import mystr
import pm
import collections

def file_to_dict_classic(fn):
  t = {}
  fin = open(fn)
  for line in fin:
    word = line.strip()
    t[word]=""

  return t


#ss = raw_input()
ss = "tigerz"

z = pm.pm()
l = mystr.file_to_list_classic("113809of.fic")
print z

z.start()
d = file_to_dict_classic("113809of.fic")
print z

print "in list"
z.start()
if ss in l:
    print ss, " in wocabulary"
else:
    print "not in wocabulary"

print z

print " "

print "=="
z.start()
for x in l:
    if x == ss:
        print ss, " in wocabulary"
        break
        
print z

print " "

print "find bisect"
z.start()
print mystr.find_bisect(l, ss)        
print z

print " "

print "in dict"
z.start()
if ss in d:
    print ss, " in wocabulary"
else:
    print "not in wocabulary"

print z
print " "

