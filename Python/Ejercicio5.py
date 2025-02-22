def calcular_promedio(calificaciones):
    suma = sum(calificaciones)
    cantidad = len(calificaciones)
    promedio = suma/cantidad
    return promedio

calificaciones = [85, 90, 78, 92, 88]

resultado = calcular_promedio(calificaciones)

print("El promedio de la calificación es: ", resultado)

print("Fin.")