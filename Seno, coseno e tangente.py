import math
a = float(input('Digite o ângulo que você deseja: '))
b = math.sin(math.radians(a))
c = math.cos(math.radians(a))
d = math.tan(math.radians(a))

print('O ângulo de {:.0f} graus, possuí um seno de {:.2f}. \n O ângulo de {:.0f} graus, possuí um cosseno de {:.2f}. \n O ângulo de {:.0f} graus, possuí uma tangente de {:.2f}.'.format(a,b,a,c,a,d))
