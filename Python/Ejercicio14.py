def calcular_polinomio(coeficientes, x):
    resultado = 0
    grado = len(coeficientes) - 1
    for i in range(len(coeficientes)):
        resultado += coeficientes[i] * (x ** (grado - i))
    return resultado

coeficientes = [4, -3, 2, -5]

print(calcular_polinomio(coeficientes, 4))

print("Fin.")