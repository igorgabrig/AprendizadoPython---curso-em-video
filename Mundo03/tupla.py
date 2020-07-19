vet = [2,1,3,4,5]

for i in vet:
    print(i)


print('\n')

for i in range(0,len(vet)):
    print(vet[i])

for pos,i in enumerate(vet):
    print(f'Na posição {pos} encontrei o valor {i}!')

print(sorted(vet))

vet[4] = 6

print(vet)