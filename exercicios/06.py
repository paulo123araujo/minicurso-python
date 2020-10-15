frase = input("Digite uma frase: ").lower()

vogais = ["a", "e", "i", "o", "u"]

qtde_vogais = 0

for i in range(0, len(frase)):
    if frase[i] in vogais:
        qtde_vogais += 1

print("Qtde de vogais na frase: %d" %(qtde_vogais))
