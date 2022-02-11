def tl(b):
    for i in b:
        x = ord(i)
        if x>=65 and x<=90:
            b = b.replace(chr(x), chr(x+32))
    print(b)                
        
b = str(input())
tl(b)


