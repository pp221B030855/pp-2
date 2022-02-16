def check(s):
    ch1=0; ch2=0; ch3=0
    for i in s:
        if i>='a' and i<='z':
            ch1+=1
        if i>='A' and i<='Z':
            ch2+=1
        if i>='0' and i<='9':
            ch3+=1  
    if ch1>0 and ch2>0 and ch3>0:
        return True
    else:
        return False                                  
# checking for the strong password
out = []
for i in range(int(input())):
    x = input()
    if check(x) and x not in out:
        out.append(x)
else:
    out = sorted(out)
    print(len(out))
    for i in out:
        print(i)