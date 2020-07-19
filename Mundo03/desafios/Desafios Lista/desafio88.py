# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

import random
from random import randint

lista = list()
jogos = list()

qtd = int(input("Quantos jogos voce quer? "))

for i in range(0,qtd):
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont>=6:
            break
    lista.sort() #ordena lista
    jogos.append(lista[:])
    lista.clear()


for i,l in enumerate(jogos): #For com enumerate para mostrar a posição e os valores
    print(f'Jogo {i+1}: {l}')

