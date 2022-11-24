a = float(input('Digite o valor do produto selecionado: R$'))
b = a * (5 / 100) #--> O valor digitado vezes a porcentagem de desconto dividido pelo 100% do produto.
c = a - b #--> O valor do produto menos o desconto.

print('O seu produto de R${:.2f} teve um desconto de 5%. \n O valor de seu desconto total é R${:.2f}. \n O novo valor de seu produto é R${:.2f}.'.format(a,b,c))