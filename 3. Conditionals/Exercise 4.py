print('Check if two words rhyme!')
word1 = input('type the word you want to compare ')
word2 = input('type the word you want to compare ')

if word1[-3:] == word2[-3:] or word1[-2:] == word2[-2:] or word1[-1:] == word2[-1:]:
    print('The words rhyme!')
else:
    print('No, try again')

print()
print('Exercise 5')
print('Elections time!\n vot for the candidate you want')
print('A --> for red party')
print('B --> for green party')
print('C --> for blue party')

vote = input('What is your vote? ')
if vote.upper()  == 'A':
    print('You voted for the red party')
elif vote.upper()  == 'B':
    print('You voted for the green party')
elif vote.upper()  == 'C':
    print('You voted for the blue party')
else:
    print('Invalid vote')