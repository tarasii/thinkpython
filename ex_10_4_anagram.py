import mystr
import pm

l = mystr.file_to_list_simple("113809of.fic")

z = pm.pm()
cnta = 0
for x in l[:10]:
    cnta = 0
    print x.strip(),
    for y in l:
        if x <> y:
            if mystr.is_anagram(x,y):
                #print x.strip(),y.strip()
                cnta += 1
        #if cnta % 100000 == 0:
        #    print ".",
    print cnta

print ""
#print len(l), cnta
print z

z.start()
cnta = 0
for x in l[:10]:
    cnta = 0
    print x.strip(),
    for y in l:
        if x <> y:
            if mystr.is_anagram_classic(x,y):
                #print x.strip(),y.strip()
                cnta += 1
        #if cnta % 100000 == 0:
            #print ".",
    print cnta
            

print ""
#print len(l), cnta
print z
