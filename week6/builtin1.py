from re import X


def multiply(ls):
    x = 1
    for i in ls:
        x*=i
    return x 

ls = list(map(int, input().split()))
print(multiply(ls))        