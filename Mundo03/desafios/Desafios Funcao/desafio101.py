# Crie um programa que tenha uma função chamada voto() 
# que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date


def voto(nasc):
    ano = date.today()

    idade = ano.year - nasc

    if idade < 16:
        return f'Com {idade} anos: Não Pode Votar'

    elif idade >= 16 and idade < 18 or idade >= 65:
        return f'Com {idade} anos: Voto Opcional'

    elif idade >= 18 and idade < 65:
        return f'Com {idade} anos: Voto Obrigatorio'




nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))