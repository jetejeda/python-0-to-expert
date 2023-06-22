print('First Exercise')
listEx1 = []
def addItem(value):
    """Add a new item to the list
    
    Params:
    value -> Any datatype
    """
    listEx1.append(value)

def getFactorial(num):
    """Get the factorial of a given number
    
    Returns a number

    Params:

    num -> positive integer
    """
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

addItem(0)
addItem(1)
addItem(4)
addItem(5)
print('List exercise', listEx1)
for i in range(len(listEx1)):
    listEx1[i] = getFactorial(listEx1[i])

print('Factorials of the list', listEx1)