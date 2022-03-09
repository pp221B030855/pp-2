import re 
s = input()
x = re.findall(r"[A-Z]{1}\w*",s)
print(x)