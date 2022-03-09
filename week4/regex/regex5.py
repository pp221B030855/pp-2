import re 
s = input()
ns  = r"\w*a+b\b"

x = re.findall(ns,s)
print(x)