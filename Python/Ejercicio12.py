def calcular_moda(lista):
    frecuencia = {}

    for numero in lista:
        if numero in frecuencia:
            frecuencia[numero] += 1
        else:
            frecuencia[numero] = 1
    moda = max(frecuencia, key=frecuencia.get)
    return moda

lista = [4, 2, 6, 7, 7, 3, 8, 8, 8]

print(calcular_moda(lista))

print("Fin.")