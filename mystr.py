def has_letters(word, letters):
  for letter in word:
    if letter in letters:
      return True
  
  return False 

def is_palindrome(word):
  if is_reverse(word,word):
    return True
  else:
    return False
  
def is_palindrome_classic(word):
 i=0
 j = len(word)-1
 while i<j:
   if word[i] != word[j]:
     return False
   i += i
   j -= j
 return True

def is_reverse(word1, word2):
  if len(word1) != len(word2):
     return False
  if word1 == word2[::-1]:
     return True
  return False

def is_reverse_classic(word1, word2):
   if len(word1) != len(word2):
      return False
   i=0
   j = len(word2)
   while j > 0:
      if word1[i] != word2[j]:
         return False
         i += i
         j -= j
         
   return True

def is_anagram_classic(word1, word2):
  for x in word1:
    if x not in word2:
      return False
 return True

def is_anagram(word1, word2):
  if set(list(word1))==set(list(word2)):
    return True
  return False

def file_to_list_simple(fn):
  fin = open(fn)
  t = list(fin)
  fin.close()  
  return t


def file_to_list_classic(fn):
  t = []
  fin = open(fn)
  for line in fin:
    word = line.strip()
    t.append(word)

  fin.close()
  return t

def file_to_list_dump(fn):
  t = []
  fin = open(fn)
  for line in fin:
    word = line.strip()
    t = t + [word]

  fin.close()
  return t
