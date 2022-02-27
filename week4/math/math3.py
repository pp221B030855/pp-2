import math 
a = int(input("Input number of sides:"))
b = int(input("Input the length of a side:"))
ab = a*b 
ang = 180/a
ang = math.radians(ang)
print (ang)
appp = (b/(2*(math.tan(ang))))
print (appp)
area =  (ab*appp*0.5)
area = round(area)
print (area)