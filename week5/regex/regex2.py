import re 
s = input()
match = re.findall(r"\w*abb\w*|\w*abbb\w*", s)
print (match)