# Faça um programa que tenha uma função chamada contador(), 
# que receba três parâmetros: início, fim e passo. 
# Seu programa tem que realizar três contagens através da função criada:

# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

def contador(inicio, fim, passo):
    print("-=-"*15)
    for i in range(inicio, fim+1, passo):
        print(f'{i}', end=' ')
    print('FIM!')
    print("-=-"*15)


contador(1, 10, 1)
contador(10, 0, -2)
print("Agora é sua vez: ")

inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

contador(inicio, fim, passo)
