global num

num = {
    'ONE' : '1',
    'TWO' : '2',
    'THR' : '3',
    'FOU' : '4',
    'FIV' : '5',
    'SIX' : '6',
    'SEV' : '7',
    'EIG' : '8',
    'NIN' : '9',
    'ZER' : '0'
}

def func(s):
    for i in range(len(num)):
        for j in num:
            if num[j]==s: return j

a = []
ans = ''; ans1 = ''
s = input(); s+=' '
for i in s:
   if len(ans)==3:
       ans1 += num[ans]
       ans=''
       if i=='+' or i==' ':
           a.append(int(ans1))
           ans1=''
           continue
   ans+=i
   
x = a[0] + a[1]; x = str(x)
for i in x:
    print(func(i), end='')