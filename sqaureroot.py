l = float(input('Enter the number that you want to square root: '))
import cmath
num_sqrt = cmath.sqrt(l)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(l,num_sqrt.real,num_sqrt.imag))