import re 
s = input()
x = re.findall("a.*b",s)
print(x)