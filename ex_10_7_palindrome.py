import pm

def has_letters(word, letters):
  for letter in word:
    if letter in letters:
      return True
  
  return False 

def is_palindrome(word):
 i=0
 j = len(word)-1
 while i<j:
   if word[i] != word[j]:
     return False
   i = i+1
   j = j-1
 return True

def is_reverse(word1, word2):
 if len(word1) != len(word2):
   return False
   i=0
   j = len(word2)
   while j > 0:
     if word1[i] != word2[j]:
       return False
       i = i+1
       j = j-1
 return True

def file_to_list_simple():
  fin = open("113809of.fic")
  t = list(fin)
  fin.close()  
  return t


def file_to_list_classic():
  t = []
  fin = open("113809of.fic")
  for line in fin:
    word = line.strip()
    t.append(word)

  fin.close()
  return t

def file_to_list_dump():
  t = []
  fin = open("113809of.fic")
  for line in fin:
    word = line.strip()
    t = t + [word]

  fin.close()
  return t


p = pm.pm()
file_to_list_simple()
print p

p.start()
file_to_list_classic()
print p

p.start()
file_to_list_dump()
print p

