"""Faça um programa que calcule a soma entre todos os números ímpares
que são multiplos de 3 e que se encontram no intervalo de 1 até 500."""



soma = 0
cont = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0: # ou tira esse 'and' e coloca for c in range (1, 501, 2)
        cont = cont + 1 # ou cont += 1
        soma = soma + c # ou soma += c
print('A soma de todos os {} valores solicitados é de {}'. format(cont, soma))
