import re 
s = "(\w*)_(\w*)"
new_s =r"\1\2"
user = input()
newus= re.sub(s, new_s, user)
print(newus)