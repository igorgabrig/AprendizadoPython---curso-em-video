# help()
# help(print)

def contador(i, f, p):
    """[Faz uma contagem e mostra na tela]

    Args:
        i ([type]): [inicio da contagem]
        f ([type]): [fim da contagem]
        p ([type]): [passo da contagem]
    """

    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


contador(0, 100, 10)
# help(contador)


def somar(a, b, c=0):  # c é um parametro opcional | Posso colocoar todos os parametros como opcional

    s = a + b + c
    print(f'A soma vale: {s}')


somar(3, 2, 5)
somar(8, 4)


def teste(b):
    b += 4
    c = 2
    print(f'a {a}')
    print(f'b {b}')
    print(f'c {c}')


a = 5
teste(2)


def testeUm(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'a {a}')
    print(f'b {b}')
    print(f'c {c}')


a = 5
testeUm(2)


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(1, 2, 3)
r2 = somar(2, 2, 3)
r3 = somar(6, 9)

print(f'Os resultados foram {r1}, {r2} e {r3}')


def fatorial(num=1):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f

num = int(input('Digite um numero: '))
print(f'O fatorial de {num} é {fatorial(num)}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um numero: '))
if par(num):
    print('É Par!!')
else:
    print('É Impar!!')