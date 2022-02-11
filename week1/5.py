def ir(x, y):
    if x > 500:
        return False
    if x <= 1:
        return False
    i = 2    
    while i*i<=x:
        if x%i==0:
            return False
        i+=1    
    if y%2!=0:
        return False 
    return True        

s = str(input())
x, y = s.split(' ')
x, y = int(x), int(y)
if ir(x, y) == True:
    print("Good job!")
else:
    print('Try next time!')
