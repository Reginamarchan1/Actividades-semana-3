def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def calcular_mcm(a, b):
    return (a * b) // gcd(a, b)

# Ejemplo de uso
numero1 = int(input("Ingresa un número: "))
numero2 = int(input("Ingresa un número: "))
mcm_resultante = calcular_mcm(numero1, numero2)
print(f"El MCM de {numero1} y {numero2} es {mcm_resultante}")

# Pregunta 1: D
# Pregunta 2: A
# Pregunta 3: C
# Pregunta 4: B
# Pregunta 5: 