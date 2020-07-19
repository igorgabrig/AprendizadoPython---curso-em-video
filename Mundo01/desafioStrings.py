nome = str(input('Seu nome: ')).strip()

print('Letras maiusculas: {}'.format(nome.upper()))
print('Letras minusculas: {}'.format(nome.lower()))
print('Total sem espaçamento: {}'.format(len(nome) - nome.count(" ")))
print('Letras do primeiro nome: {}'.format(nome.find(" ")))

nome = nome.split()

print("Ultimo nome é: {}".format(nome[len(nome)-1]))
