s = input()
delt = '.?!,:;-'
for i in delt:
    if i in s:
        s = s.replace(i, '')
s = s.split()
st = set(s)
s = list(st); s = sorted(s)
print(len(s))
for i in s:
    print(i)