# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
# da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() 
# com a mesma funcionalidade.


def leiaInt(msg):

    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um numero inteiro válido.')
            continue

        else:
            return num


def leiaFloat(msg):

    while True:
        try:
            num = float(input(msg))

        except (ValueError, TypeError):
            print('ERRO: por favor, digite um numero real válido.')
            continue
        else:
            return num


n = leiaInt('Digite um numero Inteiro: ')
print(f'Você acbou de digitar o numero {n}')

f = leiaFloat('Digite um numero Real: ')
print(f'Você acbou de digitar o numero {f}')
