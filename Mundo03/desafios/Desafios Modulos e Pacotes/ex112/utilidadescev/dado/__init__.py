
def leiaDinheiro(msg):
    flag = False
    while not flag:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO: \"{entrada}\" é um preço inválido!')
        else:
            flag = True
            return float(entrada)
