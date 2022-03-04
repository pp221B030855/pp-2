import re 
s = input()
x  = "\w*[A-Z]\w*"
nx = r"\1  \2\3"
ns = re.sub(x,nx,s)
print(ns)

