def lin():
    print('-'*30)


# def mensagem(msg):
#     print('-'*30)
#     print(f'{msg}')
#     print('-'*30)

# lin()
# print('Igor')
# lin()
# print('Gabrig')
# lin()
# print('Barboza')
# lin()


# mensagem('Igor Gabrig Barboza')
# mensagem('Curso em Python')

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------

def soma(a, b):
    s = a + b
    print(s)


soma(10, 8)
soma(b=10, a=8)


def contador(* num):
    print(num)

    print(f'Recebi os valores {num} e são ao todo {len(num)} números. ')



contador(2, 1, 7)
contador(8, 0)
contador(4, 5, 1, 3, 9)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


print("\n")
valores = [1,4,2,7,8,9,5,6]
dobra(valores)
print(valores)