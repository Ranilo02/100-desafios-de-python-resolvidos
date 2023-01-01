"""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por Km acima do limite."""

# solução 1
velocidade = int(input('Digite a velocidade: '))
multa = (velocidade - 80) * 7
if velocidade >= 81:
    print('Você ultrapassou a velocidade e vai pagar R${},00 de multa'.format(multa))



# solução 2
velocidade = float(input('Qual foi a velocidade do carrro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')