# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda 
# função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def sorteia(lista):
    for i in range(0,5):
        num = randint(0,100)
        lista.append(num)


def somaPar(lista):
    print(f'numeros sorteados: {lista}')

    soma = 0
    for i in lista:
        if(i % 2 == 0):
            soma += i
    
    print(f'A somo dos valores par desta lista é {soma}')


lista = []
sorteia(lista)
somaPar(lista)