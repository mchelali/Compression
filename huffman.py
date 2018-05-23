#!-* coding : utf-8 *-

def cmpval(x,y):
    """
      Compare 2 vals of dict
    """
    if x[1]>y[1]:
        return -1
    elif x[1]==y[1]:
        return 0
    else:
        return 1
        
        
s = {'a':0.3, 'b':0.1, 'c':0.2, 'd':0.05, 'e':0.1, 'f':0.25}
L = s.items()
print L
L.sort(cmpval)

print(L)

code ={chr(i):"" for i in range(97,97+len(s))}

l = L
print (code)

print l
while(l.__len__() > 1):
    sym = l[l.__len__()-2][0] + l[l.__len__()-1][0]
    for i in l[l.__len__()-2][0]:
        code[i] = "0"+code[i]
    for i in l[l.__len__()-1][0]:
        code[i] = "1"+code[i]
    x = l[l.__len__()-2][1] + l[l.__len__()-1][1]
    l = l[0:l.__len__()-2]
    l.append((sym, x))
    l.sort(cmpval)
    print(l)

print(sorted(code.items()))
print "code a", code['a']
