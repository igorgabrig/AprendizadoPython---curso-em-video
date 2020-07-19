# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pes = {}
pessoas = []
pesMulheres = []
idadeAcima = []

flag = 's'
pesCadastradas = 0
while flag == 's':

    pes['nome'] = str(input("Nome: "))

    while True:
        pes['sexo'] = str(input('Sexo [M/F]: ')).lower()[0]
        if pes['sexo'] in 'mf':
            break
        print('ERRO! Por favor, digite apenas M ou F')

    pes['idade'] = int(input('Idade: '))

    pessoas.append(pes.copy())

    pesCadastradas += 1

    while True:
        flag = str(input("Deseja continuar [s/n]? ")).lower()[0]
        if flag in 'sn':
            break
        print("Digite somente S ou N")

print(f'Total de pessoas cadastradas é de {pesCadastradas}') #"Ou utilizar a função len(pessoas)"

sumIdade = 0
for i in range(0, pesCadastradas):
    sumIdade += pessoas[i]['idade']

media = sumIdade/pesCadastradas

print(f'A media de idade é de {media:.2f}')


for i in range(0, pesCadastradas):                  # for p in pessoas:
    if (pessoas[i]['sexo'] == 'f'):  # ou               if p['sexo'] in 'Ff':
        pesMulheres.append(pessoas[i]['nome'])          # print(f'{p["nome"]}',end=" ")

print(f'Mulheres da lista: {pesMulheres}')

for i in range(0, pesCadastradas):
    if(pessoas[i]['idade'] > media):
        idadeAcima.append(pessoas[i]['nome'])

print(f'Pessoas com idade acima da média: {idadeAcima}')
