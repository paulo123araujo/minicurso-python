notas = input("Digite suas notas: ").split(" ")

# media = (n1 + n2 + n3) / 3
provas = len(notas)

soma_das_notas = 0
for nota in notas:
    soma_das_notas += float(nota)

media = soma_das_notas / provas
print("Sua média final é: %.2f" %(media))
