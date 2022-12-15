"""Deselvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km
e R$0,45 para viagens mais longas."""

'''distancia = int(input('Qual a distância da viagem em km? '))
p1 = distancia * 0.50
p2 = distancia * 0.45
if distancia <= 200:
    print('A passagem vai custar R${}'.format(p1))
else:
    print('A passagem vai custar R${}'.format(p2))'''

distância = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a fazer uma viagem de {}Km.'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))

#outra opção é fazer direto dessa maneira: preço = distância * 0.50 if distância <= 200 else preço = 0.45
