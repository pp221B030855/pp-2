import re
s = input()
x = re.search("[A-Z]", s)
m = x.start()
up = s[m]
up = up.lower()
ds = "_" 
ds = ds + up
print(s.replace(s[m],ds))