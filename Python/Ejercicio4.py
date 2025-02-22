def calcular_factorial(n):
    factorial = 1
    contador = 1

    while contador <= n:
        factorial *= contador
        contador += 1
    return factorial

print(calcular_factorial(5))

print("Fin.")