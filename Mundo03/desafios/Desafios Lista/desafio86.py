# Crie um programa que declare uma matriz de dimensão 3x3 
# e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

import time
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input('Numero: '))


for mat in matriz:
    print(mat) #mat é uma linha da matriz

soma = 0

for i in range(0, 3):
    for j in range(0, 3):
        if(matriz[i][j] % 2 == 0):
            soma += matriz[i][j]
        
maior = 0
for i in range(0, 3):
    if(matriz[1][i] > maior):
        maior = matriz[1][i]


print(f'A soma de todos os valores par: {soma}')
print(f'A soma dos valores da terceiro coluna é: {matriz[0][2]+matriz[1][2]+matriz[2][2]}')
print(f'O maior valor da segunda linha é: {maior}')
