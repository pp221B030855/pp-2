x = int(input())
if str(input())=='k':
    k = int(input())
    z = str(x/1024-int(x/1024))
    t = str(x/1024)
    if k==0:
        print(int(x/1024))      
    if len(z)-2<=k and k!=0:
        i=len(z)-2
        while i<k:
            t+='0'
            i+=1
        print(t)    
    else:
        print(round(x/1024, k))          
else:
    print(x*1024)
