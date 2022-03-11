import re
s = input()
x = re.findall(r"\w*[a-z]_[a-z]\w*",s)
print(x)
