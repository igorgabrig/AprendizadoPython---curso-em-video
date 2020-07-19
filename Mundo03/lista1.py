vet = [] #lista vazia ou vet = list()

for i in range(0, 8):
    # Adiciona elemento ao final da lista
    vet.append(int(input('Digite um numero: ')))


vet.sort()  # Ordena a lista em ordem crescente

vet.sort(reverse=True)  # Ordena a lista em ordem decrescente

# Adiciona elemento a lista, tendo que passar como paramentro a posição
vet.insert(2, 0)
# vet[0] = 999 #Substitui o valor da posição 0 po 999

print(vet)
print(f'Essa lista tem {len(vet)} elementos.')


vet.pop()  # elimina ultimo elemento da lista
vet.pop(2)  # elimina o elemento na posição 2 da lista

if 2 in vet:
    vet.remove(2)

print(f'Vetor novo: {vet}')


