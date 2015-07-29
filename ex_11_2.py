def histogram_classic(s):
  d = dict()
  for c in s:
    if c not in d:
      d[c] = 1
    else:
      d[c] += 1

  return d

def histogram(s):
  d = dict()
  for c in s:
    if c not in d:
      d[c] =  h.get(c, 1)

  return d

h = histogram_classic('brontosaurus')
print(h)

h = histogram('brontosaurus')
print(h)
