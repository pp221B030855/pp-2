import re 
s  = input()
x  = re.findall(r"\w*",s)
#x = re.sub('', "|",s)
n = len(x)
print (n)
i = 1
m  = n-1
p = '|'
while (i<m):
    x[i] = p
    i+=2
del x[m]
print (x)