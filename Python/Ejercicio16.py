def generar_fibonnaci(n):
    fibonnaci = [0,1]  # Inicializa la lista con los dos primeros números de la serie.
    while len(fibonnaci) < n:
        # Se agrega el siguiente elemento a la lista.
        fibonnaci.append(fibonnaci[-1] + fibonnaci[-2])
    return fibonnaci   # Retorna la lista.

resultado = generar_fibonnaci(10)  # Llamada a la función para generar los primeros 10 números de la serie.

print("Serie de Fibonnaci: ", resultado)