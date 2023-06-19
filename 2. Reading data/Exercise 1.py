import math

print('General formula to solve equations')
a = int(input('Write the a value of the formula: '))
b = int(input('Write the b value of the formula: '))
c = int(input('Write the c value of the formula: '))
bPow = pow(b, 2)-(4*a*c)
if (bPow > 0):
    answer = (-b + math.sqrt(bPow))/(2*a)
    print('Answer using the sum with the sqrt: ', answer)
    answer = (-b - math.sqrt(bPow))/(2*a)
    print('Answer using the subtraction with the sqrt: ', answer)
else:
    print('Invalid input, b**2 must be grater than 4ac')