def paln(s, s1=''):
    s1 = s[::-1]
    if s == s1: return True
    else: return False
s = input()
print(paln(s))
