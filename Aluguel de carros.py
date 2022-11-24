a = int(input('Dias utilizados: '))
b = float(input('KMs rodados: KM '))
c = (a * 60) + (b * 0.15) # --> Dividindo os kms e os dias para chegar a um resultado.

print('O valor a pagar do veiculo corresponde a R${:.2f}'.format(c))