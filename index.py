#Programa que leia a distância de uma viagem em km e calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas 
v =float(input('Diga a distância da sua vaigem:'))
if v <=200:
    print("Sua viagem irá custar: R${:.2f}".format(v * 0.50))
else:
    print('Sua viagem irá custar: R${:.2f}'.format(v*0.45))