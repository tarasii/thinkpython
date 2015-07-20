import random
import mylist

l = [random.randint(1,10) for x in range(10)]
print l
print mylist.del_duplicates_classic(l)
print mylist.del_duplicates_func(l)
