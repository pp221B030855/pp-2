import math

global o
o = input(); o = o.split()
ls = []
dc = {}
dc1 = {}
def func(x, y):
    return math.sqrt((int(o[0])-x)**2 + (int(o[1])-y)**2)

for i in range(int(input())):
    x = input(); x = x.split()
    ls.append(x)

for x in ls:
    z = func(int(x[0]), int(x[1]))
    if z in dc:
        dc1[z] = x
    else:
        dc[z] = x    

check = sorted(dc); check1 = sorted(dc1)
for x in check1: check.append(x)
check = sorted(check)  
for x in check:
    for y in dc[x]:
        print(y, end=' ')
    print()    
       