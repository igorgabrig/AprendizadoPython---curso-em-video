# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

aluno = dict()

aluno['nome'] = str(input("Nome do aluno: "))
aluno['media'] = float(input("Média: "))

if(aluno["media"] >= 60):
    
    aluno['situacao'] = 'Aprovado'

else:
    aluno['situacao'] = 'Reprovado'


print(f'O aluno {aluno["nome"]} tem a media {aluno["media"]}')
print(f'E por isso esta {aluno["situacao"]}')