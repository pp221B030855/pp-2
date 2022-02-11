s = str(input())
cnt = 0
for i in s:
    cnt+=ord(i)
if cnt > 300:
    print("It is tasty!")
else:
    print("Oh, no!")
