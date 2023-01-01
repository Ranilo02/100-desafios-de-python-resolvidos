'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
 indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''

print('{:=^40}'.format(' CONTAGEM REGRESSIVA '))
from time import sleep
time = sleep(1)
for c in range(10, -1, -1):
    sleep (1)
    print(c)
print('BUM!')