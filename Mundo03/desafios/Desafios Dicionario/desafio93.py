# Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.


jogador = {}
partida = []

jogador['nome'] = str(input("Nome: "))
jogador['partidas'] = int(input('Numero de partidas: '))

for i in range(0,jogador['partidas']):
    partida.append(int(input(f'Gols na partida {i+1}: ')))

jogador['qtdGols'] = partida[:]

soma = 0

# for j in range(0,jogador['partidas']):
#     soma += partida[j]

for item in partida:
    soma += item

#jogador['soma'] = sum(partida)
jogador['soma'] = soma

print(jogador)

for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('\n')

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')

for j in range(0,jogador['partidas']):
    print(f'Na partida {j+1}, fez {partida[j]} gols.')

print(f'Com um total de {jogador["soma"]} gols.')