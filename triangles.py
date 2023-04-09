import math
# a=leg of triangle b=leg of triangle c=hypotenuse of triangle

a = input("Enter the value of a: ")

b = input("Enter the value of b: ")

c = input("Enter the value of c: ")

print("I can find the sides of your right triangle")
a,b,c = int(a), int(b),int(c)
print(f"all sides are: {a, b, c}")

if (a == 0) and (b != 0) and (c != 0):
    a = math.sqrt(c**2 - b**2)
elif (b == 0) and (a != 0) and (c != 0): 
    b = math.sqrt(c**2 - a**2)
elif (c == 0) and (a != 0) and (b != 0): 
    c = math.sqrt(a**2 + b**2)

# this program will give you all the sides of the triangle as
# a=leg b=leg and c=hypotenuse

print(f"all sides are a, b, c : {a, b, c}")