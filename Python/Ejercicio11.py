def calcula_determinante(matriz):
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]

    determinante = (a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g))
    return determinante

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(calcula_determinante(matriz))

print("Fin.")
