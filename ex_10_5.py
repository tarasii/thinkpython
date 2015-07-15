import random

def has_duplicates_classic(l):
    for x in range(len(l)):
        for y in range(x+1, len(l)):
            if l[x] == l[y]:
                return True
    
    return False

def has_duplicates(l):
    return len(set(l))<>len(l)

def two_birthday_probability_classic(n,m):
    cnt = 1
    for j in range(0,n):
        l=[]
        for i in range(m):
            l.append(random.randint(1,365))
        #l = map(lambda(x):random.randint(1,365),range(m))
        #l = [random.randint(1,365) for x in range(m)]
        if has_duplicates(l):
            cnt += 1
    return cnt

def random_list_has_duplicates(m):
    return has_duplicates([random.randint(1,365) for z in range(m)])

def two_birthday_probability_func(n,m):
    return reduce(lambda x,y: x + 1 if random_list_has_duplicates(m) else x, range(0,n), 0)

print two_birthday_probability_classic(10000,24)
print two_birthday_probability_func(10000,24)
