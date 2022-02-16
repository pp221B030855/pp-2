x = int(input())
i=0
while i<x:
    j=0
    while j<x:
        if i==0:
            print(j, end=' ')    
        elif j==0:
            print(i, end=' ')
        elif i==j:
            print(i*i, end =' ')
        else:
            print(0, end=' ')    
        j+=1
    print('')        
    i+=1    