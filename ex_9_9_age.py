d = {}

for x in range(1, 100):
    for y in range(1, 100):
       sx = "%02d" % x
       sy = "%02d" % y
       if sx == sy[::-1] and x<y:
          delta = y-x
          if delta in d.keys():
              d[delta] += 1
          else:
              d[delta] = 1
          print sx, sy, delta

print d

