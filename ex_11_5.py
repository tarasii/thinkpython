def reverse_lookup_list(d, v):
  l = []
  for k in d:
    if d[k] == v:
      l.append(k)

  return l

def invert_dict_classic(d):
  inv = dict()
  for key in d:
    val = d[key]
    if val not in inv:
      inv[val] = [key]
    else:
      inv[val].append(key)

  return inv

def invert_dict_alt(d):
  inv = dict()
  for key in d:
    val = d[key]
    l = inv.get(val,[])
    if len(l) == 0:
      inv[val] = l

    l.append(key)

  return inv

def invert_dict(d):
  inv = dict()
  for key in d:
    val = inv.setdefault(d[key],[])
    val.append(key)

  return inv

def histogram(s):
  d = dict()
  for c in s:
     d[c] = d.get(c, 0) + 1

  return d

h = histogram('parrot')
print h
print invert_dict_classic(h)
print invert_dict_alt(h)
print invert_dict(h)
