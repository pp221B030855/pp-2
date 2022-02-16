a = list(map(int, input().split()))
i = 0
while True:
    if a[i]+i>=len(a)-1:
        print(1)
        exit()
    if a[a[i]+i]<=0 and a[i]+i!=len(a)-1:
        a[i] = a[i]-1
        if a[i]<=0:
            i-=1
            if  i<0 :
                print(0)
                exit()
    else:
        i = a[i]+i
        if i == len(a)-1:
            print(1)
            exit()