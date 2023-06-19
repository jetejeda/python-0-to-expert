print('Get the note of a student based on 3 laboratories, an exam and the final exam')
print('Formula: PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6')
print('P1, P2, and P3 are the laboratories')
print('pp is the average note of the laboratories')
print('PROM is the average total note')
print('EP is the exam and EF is the final exam')

p1 = float(input('Insert the note of the first laboratory: '))
p2 = float(input('Insert the note of the second laboratory: '))
p3 = float(input('Insert the note of the third laboratory: '))
pp = (p1+p2+p3)/3

ep = float(input('Insert the note of the exam: '))
ef = float(input('Insert the note of the final exam: '))
prom = (pp + 2*ep + 3*ef)/6

print('the student final grade is: ', prom)

