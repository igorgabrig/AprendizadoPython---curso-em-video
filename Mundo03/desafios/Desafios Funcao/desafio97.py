# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def mensagem(msg):
    tam = len(msg) + 6
    print(f'~'*tam)
    print(f'   {msg}')
    print(f'~'*tam)



mensagem('Olá, Mundo!')
mensagem('Igor Gabrig Barboza')
mensagem('Teste de Tamanho')