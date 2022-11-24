from random import shuffle

a = str(input('Aluno 1: '))
b = str(input('Aluno 2: '))
c = str(input('Aluno 3: '))
d = str(input('Aluno 4: '))

e = [a,b,c,d]
shuffle(e)

print('A ordem de apresentação da APS é: ')
print(e)