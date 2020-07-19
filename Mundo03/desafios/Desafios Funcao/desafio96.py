# Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(lar, comp):
    result = lar*comp
    print(f'A área de um terreno {lar}X{comp} é de {result}m quadrados')


largura = float(input("Largura(m): "))
comprimento = float(input("Comprimento(m): "))

area(largura, comprimento)
