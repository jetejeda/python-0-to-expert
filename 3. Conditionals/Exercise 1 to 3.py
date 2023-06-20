age = int(input('Type your age: '))

if age >= 18:
    print('You can request your ID')
else:
    print("Hey boy you shouldn't be here")

print()
print('Exercise 2')
num = int(input('Type a number and I will return its absolute value: '))
print(num.__abs__())

print()
print('Exercise 3')
letter = input('Type a letter: ')
vocals = 'aeiou'
if vocals.__contains__(letter):
    print('The letter you typed is a vocal')
else:
    print('The letter you typed is a consonant')