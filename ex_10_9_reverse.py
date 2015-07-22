import mystr
import pm

l = mystr.file_to_list_classic("113809of.fic")

def get_reverse_bisect(l):
    cnts = 0
    for x in l:
        y = x[::-1]
        if mystr.find_bisect(l, y) <> -1:
            cnts += 1
            print x,y

    print cnts

def get_reverse_classic(l):
    cnts = 0
    for x in l:
        tl = filter(lambda a: len(a)==len(x),l)
        #print tl
        for y in tl:
            if mystr.is_reverse(x,y) and not x == y:
                cnts += 1
                print x,y

    print cnts

z = pm.pm()
get_reverse_bisect(l)
print z

z.start()
get_reverse_classic(l)
print z

