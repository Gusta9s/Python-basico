a = float(input('Digite a largura de sua parede: '))
b = float(input('Digite a altura de sua parede: '))
c = a * b #--> Para descobrir seu m².

print('Sua parede de {:.0f}x{:.0f} possui uma área de {:.0f}m².'.format(a,b,c))

d = c //  2 #--> 1L de tinta pinta 2m². 

print('Para pintar sua parede de {:.0f}m², você prescisará de {:.0f}L de tinta.'.format(c,d))
