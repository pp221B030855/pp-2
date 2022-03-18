from string import ascii_lowercase, ascii_uppercase

def counter(s, cnt1=0, cnt2=0):
    for i in ascii_uppercase: cnt1 += s.count(i)
    for i in ascii_lowercase: cnt2 += s.count(i)    
    print('The number of upper case letters:', cnt1)
    print('The number of lower case letters:', cnt2)
s = 'AAAltair'
counter(s)