# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 
# 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def leiaInt(msg):
    
    while True:
        num = str(input(msg))
        if num.isnumeric():
            numero = int(num)
            return numero
        else:
            print("Digite um valor válido")


n = leiaInt('Digite um numero: ')
print(f'Você acbou de digitar o numero {n}')