from random import choice

a = str(input('Aluno 1: '))
b = str(input('Aluno 2: '))
c = str(input('Aluno 3: '))
d = str(input('Aluno 4: '))

e = [a,b,c,d]
f = choice(e)

print('O aluno escolhido foi {}.'.format(f))