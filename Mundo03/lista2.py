teste = list()
galera = list()

for i in range(0, 3):
    teste.append(str(input("Nome: ")))
    teste.append(int(input("Idade: ")))
    galera.append(teste[:])
    teste.clear()

print(galera)

for i in galera:
    if i[1] >= 18:
        print(f'{i[0]} é maior de idade.')
    
    else:
        print(f'{i[0]} é menor de idade.')


for i in range(0,len(galera)):
    print(i)