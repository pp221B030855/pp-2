dem = {}

for i in range(int(input())):
    s = input(); s = s.split()
    if s[1] in dem:
        dem[s[1]]+=1
    else:
        dem[s[1]]=1    
hun = {}

for i in range(int(input())):
    s = input(); s = s.split()
    if s[1] in hun:
        hun[s[1]]+=int(s[2])
    else:
        hun[s[1]]=int(s[2])
dleft = 0

for i in dem:
    if i in hun:
        if dem[i]>hun[i]:
            dleft+=dem[i]-hun[i]
    else:
        dleft+=dem[i]        
print('Demons left:',dleft)   