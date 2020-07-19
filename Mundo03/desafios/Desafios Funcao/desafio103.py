# Faça um programa que tenha uma função chamada ficha(), 
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, 
# mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome, gol=0):

    if nome == '':
        nome = '<desconhecido>'

    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')


nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Numero de gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0


ficha(nome, gols)
