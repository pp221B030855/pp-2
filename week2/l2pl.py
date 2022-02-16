s = input()
br = ['(', ')', '[', ']', '{', '}']
out = []
ch = False
for i in s:
    if i=='(' or i=='[' or i == '{':
        out.append(i)
    elif i==')' or i==']' or i=='}':
        if not out:
            print('No')
            exit()
        else:
            if out[len(out)-1]==br[br.index(i)-1]:
                out.pop()
            else:
                print('No')
                exit()        
if len(out)==0: print('Yes')
else: print('No') 