import random
import mylist
import pm

def random_day_generation_classic(m):
    l=[]
    for i in range(m):
        l.append(random.randint(1,365))
    return l

def random_day_generation_func(m):
    return map(lambda(x):random.randint(1,365),range(m))

def random_day_generation_list(m):
    return [random.randint(1,365) for x in range(m)]

def two_birthday_probability_classic(n,m):
    cnt = 1
    for j in range(0,n):
        if mylist.has_duplicates(random_day_generation_classic(m)):
            cnt += 1
    return cnt

def random_list_has_duplicates(m):
    return mylist.has_duplicates(random_day_generation_list(m))

def two_birthday_probability_func(n,m):
    return reduce(lambda x,y: x + 1 if random_list_has_duplicates(m) else x, range(0,n), 0)

def random_list_has_duplicates1(m):
    return mylist.has_duplicates_classic(random_day_generation_list(m))

def two_birthday_probability_func1(n,m):
    return reduce(lambda x,y: x + 1 if random_list_has_duplicates1(m) else x, range(0,n), 0)

p = pm.pm()
print two_birthday_probability_classic(10000,24)
print p
p.start()
print two_birthday_probability_func(10000,24)
print p
p.start()
print two_birthday_probability_func1(10000,24)
print p

