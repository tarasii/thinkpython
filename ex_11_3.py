def histogram(s):
  d = dict()
  for c in s:
    d[c] =  d.get(c, 0) + 1

  return d

h = histogram('brontosaurus')
print(h)

def print_hist(h):
  for c in h:
    print(c, h[c])

#print_hist(h)

def print_hist_sort(h):
  l = h.keys()
  l.sort()
  for c in l:
    print(c, h[c])

print_hist_sort(h)
