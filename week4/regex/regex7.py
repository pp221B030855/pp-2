import re
s = input()
x = re.search("_", s)
m = x.start()
up = s[m+1]
up = up.upper()
print(s.replace(s[m:m+1],up))