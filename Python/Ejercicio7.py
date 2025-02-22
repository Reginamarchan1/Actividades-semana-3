def calcular_mediana(numeros):
    numeros.sort()
    n = len(numeros)

    if n % 2 == 1:
        mediana = numeros[n//2]
    else:
        mediana = (numeros[n // 2 - 1] + numeros[n // 2]) / 2
    return mediana    

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = calcular_mediana(numeros)
print("La mediana es: ", resultado)

print("Fin.")
