def imprime_linha(n):
    linha = ""

    for i in range(0,n):
        linha += f"{n} "

    return linha

numero = int(input("Digite um número: "))

for i in range(1, numero+1):
    print(imprime_linha(i))
