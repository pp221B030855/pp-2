def palindrome(s, s1=''):
    s1 = s[::-1]
    if s == s1: return True
    else: return False
s = 'OTTO'
print(palindrome(s))
