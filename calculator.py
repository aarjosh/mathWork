#calculator
def addition(firstnum, secondnum):
  print(firstnum+secondnum)

def subtraction(firstnum, secondnum):
  print(firstnum - secondnum)

def multiplication(firstnum, secondnum):
  print(firstnum * secondnum)

def division(firstnum, secondnum):
  print(firstnum/secondnum)

num = 0
firstnum = 0
secondnum = 0
gone = 0

calc = "n"
num = int(input("How many numbers will you input?"))
for i in range(num):
  firstnum = int(input("Number"))
  gone += 1
  if gone < num:
    function = input("Which function would you like to do? Type a for addition, s for subtraction")
    if function == "a":
      secondnum += firstnum
    elif function == "s":
      secondnum -= firstnum

print(secondnum)
     