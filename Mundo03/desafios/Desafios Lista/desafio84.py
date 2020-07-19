# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoa = list()  # Cria lista vazia Pessoa
geral = list()  # Cria lista vazia Geral que ira receber pessoa
pesPesada = list()  # Lista vazia para guardas as pessoas mais pesadas
pesLeve = list()  # Lista vazia para guardas as pessoas mais leves
maior = menor = 0  # Variaveis inicializadas com o valor 0

continua = str(input("Deseja cadastrar uma pessoa, S ou N: ")).lower()

while continua == 's':

    pessoa.append(str(input('Nome: ')))  # Adiciona nome a lista pessoa
    pessoa.append(float(input('Peso: ')))  # Adiciona peso a lista pessoa

    if(len(geral) == 0):  # Se a lista composta Geral, estiver vazia, atribui as variaveis maior e menor o peso da primeira pessoa cadastrada em Pessoa
        maior = menor = pessoa[1]
    else:
        if(pessoa[1] > maior):
            maior = pessoa[1]
        if(pessoa[1] < menor):
            menor = pessoa[1]

    geral.append(pessoa[:])  # Atribui a lista Pessoa a Geral como copia "[:]"
    pessoa.clear()  # Apaga pessoa
    continua = str(input("Deseja continuar? S/N: ")).lower()


for pes in geral:
    if(pes[1] == maior):
        pesPesada.append(pes[0])
    if(pes[1] == menor):
        pesLeve.append(pes[0])

print(f'foram cadastradas {len(geral)} pessoas')
print(f'O maior peso foi de {maior}. Peso de {pesPesada}')
print(f'O menor peso foi de {menor}. Peso de {pesLeve}')
