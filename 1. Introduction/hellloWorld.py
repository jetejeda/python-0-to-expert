print("Hey!")

'''Comment 
using multiple
lines'''

print(((3+2)/(2*5))**2)

clownWeight = 112#grams
dollWeight = 75#grams
clownQty = 23
dollQty = 54
print(clownWeight*clownQty + dollWeight*dollQty)

#First exercise with strings
firstLine = 'First exercise with python strings'

print("Print the first two characters: " + firstLine[:2])
print("Print the last three characters: " + firstLine[-3:])
print("Print all even index characters: " + firstLine[: : 2])
print("Print it backwards: " + firstLine[0:-1])
print("To print a string backwards: " + firstLine[: : -1])
print("Print the string and its reflect: ", firstLine + ' ' + firstLine[: : -1])

secondExercise = 'Separated'
char = ','
#mix the secondExercise string and char
print('Mixing the characters: ', secondExercise.replace('',char)[1:-1])
