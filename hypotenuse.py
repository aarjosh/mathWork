import math

print("We are here to help find side of triangles A and B are shorter sides of triangle and C is potenuse.")
res = input("Are you trying to find the potenuse of the triangle.(Y/N)")
if (res == "Y"):
    a = float(input("a: "))
    b = float(input("b: "))
    c = math.sqrt(a**2 + b**2)
else:
    print("Input the lengths of the shorter triangle sides:")
    a = float(input("shorter leg of triangle a: "))
    c = float(input("Enter hypotenuse of triangle c: "))
    b = math.sqrt(c**2 - a**2)

print(f"The three sides of the right angle triangle are \n A: {a}\n B: {b}\n C: {c}")
