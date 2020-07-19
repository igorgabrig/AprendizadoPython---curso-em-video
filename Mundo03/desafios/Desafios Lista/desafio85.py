#  Crie um programa onde o usuário possa digitar sete valores numéricos e 
#  cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
#  No final, mostre os valores pares e ímpares em ordem crescente.

num = [[], []] #Inicializa lista composta num ja atribuindo espaços separados para impares e pares
valor = 0

for n in range(0,7):
    valor=int(input("Digite um valor: "))
    if((valor % 2) == 0):
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort()
num[1].sort()
print(f'Paras: {num[0]}')
print(f'Impares: {num[1]}')

print(num[0][1])