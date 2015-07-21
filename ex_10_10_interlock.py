import mystr
import pm

def find_interlock():
    cnts = 0
    for x in l:
        if mystr.is_interlock(l,x):
            cnts += 1
            print x , x[::2], x[1::2]

    print cnts

def find_triple_interlock():
    cnts = 0
    for x in l:
        if mystr.find_bisect(l,x[::3])<>-1 and mystr.find_bisect(l,x[1::3])<>-1 and mystr.find_bisect(l,x[2::3])<>-1:
            cnts += 1
            print x,x[::3],x[1::3],x[2::3]

    print cnts

l = mystr.file_to_list_classic("113809of.fic")

z = pm.pm()
find_interlock()
print z

z.start()
find_triple_interlock()
print z

