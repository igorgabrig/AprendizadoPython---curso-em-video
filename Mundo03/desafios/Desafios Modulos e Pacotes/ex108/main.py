#Adapte o código do desafio #107, criando uma função adicional chamada moeda() 
# que consiga mostrar os números como um valor monetário formatado.

import moeda

valor = float(input('Digite um valor: '))

print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {valor} é {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentando em 10%, temos {moeda.moeda(moeda.aumentar(valor))}')
print(f'Diminuindo em 10%, temos {moeda.moeda(moeda.diminuir(valor))}')
