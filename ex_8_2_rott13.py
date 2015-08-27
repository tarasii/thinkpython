import mystr
import pm


def rotate_word(word, n):
  res = ""
  a = ord("a")
  z = ord("z")
  for x in word.lower():
    #rint x, ord(x),
    t = ord(x) + n
    if t > z:
      t = t - z + a - 1
    elif t < a:
      t = t + z - a + 1
    print t

    res += chr(t)
  return res

  
#z = pm.pm()
#l = mystr.file_to_list_classic("113809of.fic")
#print z


#z.start()
w = "testzaby"
print "%s -> %s" % (w, rotate_word(w,1))
print "%s -> %s" % (w, rotate_word(w,-1))
#print z
w = "cheer"
print "%s -> %s" % (w, rotate_word(w,7))

w = "melon"
print "%s -> %s" % (w, rotate_word(w,-10))

#print len(rl)
#print rl

