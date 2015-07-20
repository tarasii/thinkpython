import mystr
import pm
import collections

l = mystr.file_to_list_classic("113809of.fic")

#ss = raw_input()
ss = "tiger"

z = pm.pm()
if ss in l:
    print ss, " in wocabulary"
else:
    print "not in wocabulary"
print z

z.start()
for x in l:
    if x == ss:
        print ss, " in wocabulary"
        
print z

def find_bisect(wocab_list, word):
    cnt = 1
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
        cnt += 1

    if wocab_list[tmp] <> word and wocab_list[begin_lim] <> word and wocab_list[end_lim] <> word:
        tmp = -1
    elif wocab_list[begin_lim] == word:
        tmp = begin_lim
    elif wocab_list[end_lim] == word:
        tmp = end_lim

    return [tmp, cnt]

z.start()
print find_bisect(l, ss)        
print z

#r = []
#for x in l[:1000]:
#    r.append(find_bisect(l,x)[1])

r = map(lambda a: find_bisect(l, a)[1], l)

#d = {}
#for x in r:
#    if x in d:
#        d[x] += 1
#    else:
#        d[x] = 1
        
#print d

cn = collections.Counter(r)
print cn
