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
  for x in word2:
    if x not in word1:
      return False
    
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

def words_no_letters(wocab, letters):
  res = []
  for x in wocab:
  if not mystr.has_letters(x, letters):
    res.append(x)
  return res

def words_no_letters_func(wocab, letters):
  return filter(lamda a: not mystr.has_letters(a, letters), wocab)

def is_interlock(wocab_list, word):
  word_odd = word[::2]
  word_even = word[1::2]
  return find_bisect(wocab_list, word_odd) <> -1 and find_bisect(wocab_list, word_even) <> -1  

def find_bisect(wocab_list, word):
    end_lim = len(wocab_list) - 1
    begin_lim = 0
    last_tmp = 0
    tmp = begin_lim +(end_lim - begin_lim) / 2
    while last_tmp <> tmp and wocab_list[tmp] <> word and wocab_list[begin_lim] <> word and wocab_list[end_lim] <> word:
        #print wocab_list[tmp], cnt, begin_lim, end_lim
        if word > wocab_list[tmp]:
            begin_lim = tmp
        else:
            end_lim = tmp

        last_tmp = tmp
        tmp = begin_lim +(end_lim - begin_lim) / 2

    if wocab_list[tmp] <> word and wocab_list[begin_lim] <> word and wocab_list[end_lim] <> word:
        tmp = -1
    elif wocab_list[begin_lim] == word:
        tmp = begin_lim
    elif wocab_list[end_lim] == word:
        tmp = end_lim

    return tmp
