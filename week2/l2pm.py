x = True
date = []
date1 = {}
while x:
    s = input(); x = s.split()
    check = ''
    if x[0]=='0':
        break
    check+=x[2]; check+=x[1]; check+=x[0]
    date.append(check); date1[check] = s
date = sorted(date)
for i in date:
    print(date1[i])