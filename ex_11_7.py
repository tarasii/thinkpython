import random
import mylist
import pm

def random_list_generation_classic(m):
    l=[]
    for i in range(m):
        l.append(random.randint(1,100000))
    return l

def has_duplicates_dict(l):
   d = {}
   for x in l:
     if x in d:
       return True 

     d[x] = True

   return False

z = pm.pm()
l = random_list_generation_classic(100000)
print z
#print l

z.start()
print mylist.has_duplicates_classic(l)
print z

z.start()
print has_duplicates_dict(l)
print z
