def segundo_mayor(lista):
    lista = list(set(lista))
    lista.sort(reverse=True)
    return lista[1] if len(lista) > 1 else None

print(segundo_mayor([1, 2, 3, 4, 5, 6]))

print("Fin.")
