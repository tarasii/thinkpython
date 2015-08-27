import mystr
import pm


def rotate_word(word, n):
  res = ""
  a = ord("a")
  z = ord("z")
  for x in word.lower():
    t = ord(x) + n
    if t > z:
      t = t - z + a - 1
    elif t < a:
      t = t + z - a + 1
    print t
    #print x, ord(x), t

    res += chr(t)
  return res

  
w = "testzaby"
print "%s -> %s" % (w, rotate_word(w,1))
print "%s -> %s" % (w, rotate_word(w,-1))

w = "cheer"
print "%s -> %s" % (w, rotate_word(w,7))

w = "melon"
print "%s -> %s" % (w, rotate_word(w,-10))
