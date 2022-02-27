import math 
a = int(input("Input number of sides:"))
b = int(input("Input the length of a side:"))
a = math.radians(a)
p = 3.14159
mal = p / a
rad =  (math.tan(mal))
print(rad)
rad = b/2*rad
print (rad)
print(a*b*rad*0.5)
