# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)

def notas(* notas, situacao = False):

    infos = dict()
        
    infos['qtd'] = len(notas)
    infos['maior'] = max(notas)
    infos['menor'] = min(notas)
    infos['media'] = sum(notas) / len(notas)
    
    if situacao == True:

        if infos['media'] >= 8:
            infos['situacao'] = 'Otima'
        elif infos['media'] >= 6:
            infos['situacao'] = 'Boa'
        elif infos['media'] < 6:
            infos['situacao'] = 'Ruim'

    return infos




print(notas(9,8,8.5,9, situacao=True))
    

