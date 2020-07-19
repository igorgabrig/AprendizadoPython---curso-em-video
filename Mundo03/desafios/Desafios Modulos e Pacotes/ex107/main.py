# Crie um módulo chamado moeda.py que tenha as funções incorporadas 
# aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

valor =  float(input('Digite um valor: '))

print(f'A metade de {valor} é {moeda.metade(valor)}')
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'Aumentando em 10%, temos {moeda.aumentar(valor)}')
print(f'Diminuindo em 10%, temos {moeda.diminuir(valor)}')
