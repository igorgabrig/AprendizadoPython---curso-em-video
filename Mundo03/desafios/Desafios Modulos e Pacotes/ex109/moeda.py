def aumentar(valor=0, taxa = 0, formato = False):
    
    valor += (valor * (taxa)/100)
    
    if formato:
       return moeda(valor)

    
    return valor


def diminuir(valor=0, taxa = 0, formato = False):
    valor -= (valor * (taxa/100))
    
    if formato:
       return moeda(valor)

    return valor


def dobro(valor=0, formato = False):
    valor *= 2

    if formato:
       return moeda(valor)

    return valor


def metade(valor, formato = False):
    valor /= 2

    if formato:
       return moeda(valor)

    return valor


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
