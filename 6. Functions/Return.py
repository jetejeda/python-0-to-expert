def graterThan(num1, num2):
    """Indicate which number is grater.
    return options:
    1 ->  num1 > num2
    -1 -> num1 < num2
    0 -> num1 == num2

    params:
    num1 and num2 are integers
    """
    result = 0
    if num1 > num2:
        result = 1
    else:
        result = -1 if num1 < num2 else 0
    return result

print('FirstExercise')
num1 = int(input('Type the first number: '))
num2 = int(input('Type the second number: '))

print('The greatest number is: ', graterThan(num1, num2))