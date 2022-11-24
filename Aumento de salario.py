a = float(input('Digite seu salario: R$'))
b = a * (15/100) # --> Para formatarmos como porcentagem!.
c = a + b # --> Para somarmos o aumento!.

input('O seu salario de R${:.2f} recebeu um aumento de 15% que equivale há R${:.2f}. \n Seu novo salario depois deste aumento equivale há {:.2f}'.format(a,b,c))