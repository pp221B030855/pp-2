from re import X
def mult(ls):
    x = 1
    for i in ls:
        x*=i
    return x 
ls = list(map(int, input().split()))
print(mult(ls))        