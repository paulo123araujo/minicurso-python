peso_peixes = int(input("Digite quantos kilos de peixe você pegou: "))

limite = 50
multa_por_kilo = 4.00

if peso_peixes < limite:
    print(f"Peixes em kilo: {peso_peixes}kg")
else:
    excessao = peso_peixes - limite
    total_multa = excessao * multa_por_kilo
    print(f"Peixes em kilo: {peso_peixes}kg")
    print(f"Excedeu {excessao} kilos")
    print(f"Valor da multa a pagar: R$ {total_multa}")
