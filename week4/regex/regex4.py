import re 
s = input()
x = re.findall(r"[A-Z]\w*",s)
print(x)