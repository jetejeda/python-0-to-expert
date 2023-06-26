class Calculator():
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    @property
    def num1(self):
        return self._num1
    
    @property
    def num2(self):
        return self._num2
    
    def sum(self):
        return self._num1 + self._num2
    
    def subtract(self):
        return self._num1 - self._num2
    
    def multiply(self):
        return self._num1 * self._num2
    
    def divide(self):
        if self._num2 != 0:
            return self._num1 / self._num2
        else:
            return 0

calc = Calculator(6,3)
print('The result from summing the numbers {} + {} is: {}'.format(calc.num1, calc.num2, calc.sum()))
print('The result from subtracting the numbers {}  {} is: {}'.format(calc.num1, calc.num2, calc.subtract()))
print('The result from multiplying the numbers {} * {} is: {}'.format(calc.num1, calc.num2, calc.multiply()))
print('The result from dividing the numbers {} / {} is: {}'.format(calc.num1, calc.num2, calc.divide()))
