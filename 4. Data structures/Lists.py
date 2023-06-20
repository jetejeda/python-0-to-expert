print('First Exercise')
print('Adding elements at the beginning of a list')
listEx1 = [20, 50, 'Course', 'python', 3.14]
print('Original list: ', listEx1)

listEx1.insert(0, input('Type the first value that you want to include at the beginning of the list: '))
listEx1.insert(1, input('Type the second value that you want to include at the beginning of the list: '))
print('New list: ', listEx1)

print()
print('\n Second Exercise')
print('There is a list with the values from 1 to 10, the values in which their index is 4,7 and 9 (zero based indexes) should be multiplied by 2')
listEx2 = [1,2,3,4,5,6,7,8,9,10]
multiplier = 2
print('Original list: ', listEx2)
listEx2[4] *= multiplier
listEx2[7] *= multiplier
listEx2[9] *= multiplier
print('New list: ', listEx2)