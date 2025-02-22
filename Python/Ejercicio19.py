import random

def generar_numeros_aleatorios(n):
    lista = list()
    for i in range(n):
        lista.append(random.randint(1, 100))
    return lista

resultado = generar_numeros_aleatorios(100)
print("Números aleatorios:", resultado)

# Pregunta 1: C
# Pregunta 2: A
# Pregunta 3: C
# Pregunta 4: A
# Pregunta 5: 