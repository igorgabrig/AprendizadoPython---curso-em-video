#pessoas = {'nome': 'Igor', 'sexo': 'M', 'idade': 23}

# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') #No valor a ser buscado no parametro tem de estar entre aspas ""

# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())

# for k in pessoas.keys():
#     print(k)

# for v in pessoas.values():
#     print(v)

# for i in pessoas.items():
#     print(i)

# for k,v in pessoas.items():
#     print(f'{k} = {v}')

# del pessoas['sexo']

# pessoas['nome'] = 'Leandro'

# pessoas['peso'] = 70

# for k,v in pessoas.items():
#     print(f'{k} = {v}')


# brasil = []  # lista vazia, esquivalente a ----> brasil = list()
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)

# print(brasil)
# print(brasil[0])
# print(brasil[0]['uf'])
# print(brasil[1]['sigla'])

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input("Estado: "))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())

print("\n")

for e in brasil:
    print(e)

print("\n")
for e in brasil:
    for k, v in e.items():
        print(f'{k} = {v}')

print("\n")
for e in brasil:
    for v in e.values():
        print(f'{v}', end=' ')
    print()