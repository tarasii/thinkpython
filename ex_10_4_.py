import mystr
import pm

l = mystr.file_to_list_simple("113809of.fic")

x = raw_input()

z = pm.pm()

cnta = 0
for y in l:
    ys = y.strip()
    if x <> ys:
        if mystr.is_anagram_classic(x,ys):
            print x,ys
            cnta += 1
    #if cnta % 100000 == 0:
        #print ".",
print cnta
            

print ""
#print len(l), cnta
print z
