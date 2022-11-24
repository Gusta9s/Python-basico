from math import sqrt, ceil
a = int(input('Digite um número: '))
b = sqrt(a)

print('A raiz quadrada de {:.0f} é igual há {:.0f}.'.format(a, ceil(b)))