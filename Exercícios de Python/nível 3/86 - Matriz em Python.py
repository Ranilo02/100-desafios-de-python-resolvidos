"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""
# soluçaõ 1

# matriz = [[], [], []]
# for c in range (0, 3):
#     n1 = int(input(f'Digite um valor para [0, {c}]: '))
#     matriz[0].append(n1)
# for c in range (0, 3):
#     n2 = int(input(f'Digite um valor para [1, {c}]: '))
#     matriz[1].append(n2)
# for c in range (0, 3):
#     n3 = int(input(f'Digite um valor para [2, {c}]: '))
#     matriz[2].append(n3)
#
# for c in matriz[0]:
#     print(f'[ {c} ]', end='')
# print()
# for c in matriz[1]:
#     print(f'[ {c} ]', end='')
# print()
# for c in matriz[2]:
#     print(f'[ {c} ]', end='')

# solução 2 (p)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:  '))

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
