x = int(input())
s = input(); s = s.split()
i = 0
max = -99999999999
while i<x:
    j=0
    while j<x:
        if j==i:
            j+=1
            continue
        else:
            if max<int(s[i])*int(s[j]):
                max = int(s[i])*int(s[j])
        j+=1
    i+=1    
print(max)