c = {}
st = []
num = int(input())
max = -100
for i in range(num):
    s = input(); 
    s = s.split()
    if s[0] in c:
        c[s[0]]+=int(s[1])
        if max<c[s[0]]:
            max = c[s[0]]
    else:
        c[s[0]] = int(s[1])
        st.append(s[0]) 
        if max<c[s[0]]:
            max = c[s[0]]         
st = sorted(st)
for i in st:
    if  c[i]==max:
        print(i, 'is lucky!')
    else:
        print(i, 'has to receive {} tenge' .format(max-c[i]))