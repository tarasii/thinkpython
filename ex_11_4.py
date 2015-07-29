def reverse_lookup_list(d, v):
  l = []
  for k in d:
    if d[k] == v:
      l.append(k)

  return l

def histogram(s):
  d = dict()
  for c in s:
     d[c] = d.get(c, 0) + 1

  return d

h = histogram('parrot')
print h
print reverse_lookup_list(h, 1)
print reverse_lookup_list(h, 2)
print reverse_lookup_list(h, 3)
