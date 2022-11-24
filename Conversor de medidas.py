a = float( input('Digite um valor em metros: '))
b = a * 0.001 #--> Quilómetro
c = a * 0.01 #--> Hectômetro
d = a * 0.1 #--> Decâmetro
e = a * 10 #--> Decímetro
f = a * 100 #--> Centímetros 
g = a * 1000 #--> Milímetros


print('Sua medida {:.0f}m corresponde: \n {:.3f}km Quilómetros; \n {:.2f}hm Hectômetros; \n {:.1f}dam Decâmetros; \n {:.0f}dm Decímetros; \n {:.0f}cm Centímetros; \n {:.0f}mm Milímetros.'.format(a,b,c,d,e,f,g))