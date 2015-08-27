import mystr
import pm

def rotate_letter(letter, n):
  x = ord(letter) + n
  if x > letter_z:
    x = x - letter_number
  elif x < letter_a:
    x = x + letter_number
    
  return chr(x)

def rotate_word(word, n):
  res = ""
  a = ord("a")
  z = ord("z")
  for letter in word.lower():
    res += rotate_letter(letter, n)
    
  return res


letter_a = ord("a")
letter_z = ord("z")
letter_number = letter_z - letter_a + 1
  
  
w = "testzaby"
print "%s -> %s" % (w, rotate_word(w,1))
print "%s -> %s" % (w, rotate_word(w,-1))
print "%s -> %s" % (w, rotate_word(w,25))

w = "cheer"
print "%s -> %s" % (w, rotate_word(w,7))

w = "melon"
print "%s -> %s" % (w, rotate_word(w,-10))
