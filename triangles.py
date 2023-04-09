import math


a = input("Enter the value of one side of triangle: ")

b = input("Enter the value of second side of triangle: ")

c = input("Enter the value of third side of triangle: ")

print("I can check if triagle has right angle or not!!!!")
a,b,c = int(a), int(b),int(c)
print(f"all sides are: {a, b, c}")

if (a == 0) and (b != 0) and (c != 0):
    a = math.sqrt(c**2 - b**2)
elif (b == 0) and (a != 0) and (c != 0): 
    b = math.sqrt(c**2 - a**2)
elif (c == 0) and (a != 0) and (b != 0): 
    c = math.sqrt(a**2 + b**2)


print(f"all sides are: {a, b, c}")