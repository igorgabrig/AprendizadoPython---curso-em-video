# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar 
# as notas de cada aluno individualmente.


aluno = list()
alunos = list()


while True:
    aluno.append(str(input("Nome: ")))
    aluno.append(float(input("Nota 1: ")))
    aluno.append(float(input("Nota 2: ")))

    media = ((aluno[1] + aluno[2]) / 2)
    aluno.append(media)

    alunos.append(aluno[:])
    aluno.clear()

    cont = str(input('Deseja continuar? S ou N: ')).lower()
    if(cont == 'n'):
        break


for i, a in enumerate(alunos):
    print(f'{i} - {a[0]}: {a[3]}')

cont = 0
while True:
    pes = int(input("Mostrar nota de qual alunos? "))

    if pes <= len(alunos)-1:
        print(f'Nota de {alunos[pes][0]} é: 1- {alunos[pes][1]} 2- {alunos[pes][2]}')

    if pes == 999:
        break
