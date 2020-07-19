# Crie um programa que tenha uma função fatorial()
# que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela 
# o processo de cálculo do fatorial.

def fatorial(num, show=False):

    resultado = 1

    for fat in range(num, 0, -1):
        if show:
            print(fat, end='')
            if fat > 1:
                print(' x ', end = '')
            else:
                print(' = ', end='')
        resultado *= fat
    
    return resultado


print(fatorial(5, True))
