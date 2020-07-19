# Aprimore o desafio 93 para que ele funcione com vários jogadores, 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = {}
partida = []
jogadores = []

while True:
    jogador['nome'] = str(input("Nome: "))
    jogador['partidas'] = int(input('Numero de partidas: '))

    for i in range(0, jogador['partidas']):
        partida.append(int(input(f'Gols na partida {i+1}: ')))

    jogador['qtdGols'] = partida[:]
    jogador['total'] = sum(jogador['qtdGols'])
    partida.clear()

    jogadores.append(jogador.copy())

    while True:
        flag = str(input('Deseja continuar? [S/N]: ')).lower()[0]

        if flag in 'sn':
            break
        print('Digite apensa Sim(S) ou Não(N)')
    print("--"*15)
    if flag == 'n':
        break
    

print(jogadores)
print("-==-"*20)

print('cod', end='  ')

for i in jogador.keys():
    print(f'{i:<15}', end='')

print()
print("--"*40)
for k,v in enumerate(jogadores):
    print(f'{k:>3} ', end =' ') #k:>3 --> Chave com 3 caracteres, centralizado a direita
    for d in v.values():
        print(f'{str(d):<15}', end = '')
    print()
print('--'*40)

while True:
    search = int(input("Deseja mostrar dados de qual jogador? "))
    if search == 999:
        print("See you!!")
        break
    if(search >= len(jogadores)):
        print("Por favor, digite um codigo válido!")
    else:
        print(f'---Jogador {jogadores[search]["nome"]}---')
        for k,v in enumerate(jogadores[search]['qtdGols']):
            print(f'No {k+1}° jogo fez {v} gols')

        print('--++==--'*20)