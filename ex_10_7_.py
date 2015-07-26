import pm
import mystr

def file_to_list_dump():
  t = []
  fin = open("113809of.fic")
  for line in fin:
    word = line.strip()
    t = t + [word]

  fin.close()
  return t


p = pm.pm()
mystr.file_to_list_simple()
print p

p.start()
mystr.file_to_list_classic()
print p

p.start()
file_to_list_dump()
print p



