import time 

num = int(input())
st = int(input())
time.sleep(st/1000)
print('Square root of {} after {} miliseconds is {}' .format(num, st, num**0.5))