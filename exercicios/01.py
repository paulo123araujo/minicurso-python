numeros = input("Digite dois números: ").split(" ")

num1 = float(numeros[0])
num2 = float(numeros[1])

# print(f"{num1} + {num2} = {num1 + num2}")

print("%.2f + %.2f = %.2f" %(num1, num2, (num1 + num2)))

# print(num1, "+", num2, "=", num1 + num2)
print(num1, "-", num2, "=", num1 - num2)
print(num1, "*", num2, "=", num1 * num2)
print(num1, "/", num2, "=", num1 / num2)

