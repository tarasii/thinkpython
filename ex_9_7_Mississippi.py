import pm
import mystr

p = pm.pm()
cntd = 0
cntdd = 0
cntddd = 0
l = mystr.file_to_list_simple("113809of.fic")

for x in l:
  for i in range(len(x)-1):
    if x[i]==x[i+1]:
      #print x
      cntd += 1
print len(l), cntd, cntdd, cntddd

cntd = 0
for x in l:
  for i in range(len(x)-3):
    if x[i]==x[i+1]:
      #print x
      cntd += 1
      if x[i+2]==x[i+3]:
        cntdd += 1
print len(l), cntd, cntdd, cntddd

cntdd = 0        
cntd = 0
for x in l:
  for i in range(len(x)-5):
    if x[i]==x[i+1]:
      #print x
      cntd += 1
      if x[i+2]==x[i+3]:
        cntdd += 1
        if x[i+4]==x[i+5]:
          print x
          cntddd += 1
        
print len(l), cntd, cntdd, cntddd
print p
