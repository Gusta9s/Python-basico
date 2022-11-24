import math
a = int(input('Digite um número: '))
b = math.sqrt(a)

print('A raiz quadrada de {:.0f} é igual há {:.0f}.'.format(a, math.ceil(b)))