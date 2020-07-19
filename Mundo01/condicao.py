velocidade = float(input("Velocidade: "))

if (velocidade >= 80) :
    print("Multa de: {:.3}".format((velocidade-80)*7))
else:
    print("Sem multa")