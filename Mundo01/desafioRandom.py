import random

a1 = str(input("Aluno 1: "))
a2 = str(input("Aluno 2: "))
a3 = str(input("Aluno 3: "))
a4 = str(input("Aluno 4: "))

vet = [a1, a2, a3, a4]

print("O aluno será: {}".format(random.choice(vet)))

random.shuffle(vet)

print("A ordem será: {}".format(vet))
