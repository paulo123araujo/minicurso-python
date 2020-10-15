def calcula_fatorial(n):
    resultado = 1

    for i in range(1, n+1):
        resultado = resultado * i

    return resultado

def imprime_numeros(n):
    imprimir = ""

    for i in range(n, 0, -1):
        imprimir += "%d . " %(i)

    return imprimir[:len(imprimir) - 3]

numero = int(input("Digite um numero: "))

print("Fatorial de: %d" %(numero))

imprime = imprime_numeros(numero)
fatorial = calcula_fatorial(numero)

print("%d! = %s = %d" %(numero, imprime, fatorial))
