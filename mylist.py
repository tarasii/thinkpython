def dell_val_from_list(l,x):
  res = []
  for y in l:
    if y <> x:
      res.append(y)
  return res

def dell_val_from_list_func(l,x):
  return filter(lambda a: a != x, l)

def is_sorted(l):
    p = l[0];
    for x in l[1:]:
        if p <= x:
            p = x
        else:
            return False

    return True

def chop(l):
    del l[0]
    del l[-1]
    return None

def middle(l):
    return l[1:-1]


def has_duplicates_classic(l):
    for x in range(len(l)):
        for y in range(x+1, len(l)):
            if l[x] == l[y]:
                return True
    
    return False

def has_duplicates(l):
    return len(set(l))<>len(l)

def del_duplicates_func(l):
    res = []
    map(lambda a: res.append(a) if a not in res else None, l)
    #[res.append(x) for x in l if x not in res]
    return res

def del_duplicates_classic(l):
    res = []
    for x in l:
        if not x in res:
            res.append(x)
    
    return res

