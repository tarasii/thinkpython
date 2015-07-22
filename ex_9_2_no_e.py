import mystr
import pm

l = mystr.file_to_list_classic("113809of.fic")

letters = "e"
  
z = pm.pm()
rl = mystr.words_no_letters(l, letters)
print z

cnt = len(l)
cnt_e = len(rl)
pers = cnt_e * 100 / cnt 
print "total words %d, words with no %s %d, this is %d%%" % (cnt,letters,cnt_e,pers)



z.start()
rl = mystr.words_no_letters_func(l,"e")
print z

cnt = len(l)
cnt_e = len(rl)
pers = cnt_e * 100 / cnt 
print "total words %d, words with no %s %d, this is %d%%" % (cnt,letters,cnt_e,pers)
