from math import hypot
a = float(input('Comprimento do cateto oposto: '))
b = float(input('Comprimento do cateto adjacente: '))
c = hypot(a,b)

print('O comprimento da hipotenusa é {:.2f}.'.format(c))