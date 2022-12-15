"""Faça um programa que leia o peso de 5 pessoas.
No final, mostre qual foi o maior e o menor peso lidos."""
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {}ª em Kg: '.format(p)))
    if p == 1:   #o numero 1 significa que está sendo lido o primeiro resultado, o peso da primeira pessoa   # IMPORTANTE: Quando eu quero saber o maior ou o menor, eu preciso primeiro verificar se é o primeiro que sair, e ele sempre vai ser o maior e o menor, pois enquanto só houver um resultado, ele será ambos.
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\nO maior peso encontrado foi de {}Kg'.format(maior))
print('O menor peso encontrado foi de {}Kg'.format(menor))