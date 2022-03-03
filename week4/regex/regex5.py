import re 
s = input()
x = re.findall(r"\w*a\w*b",s)
print(x)