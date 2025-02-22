def juego_adivinanza():
    bajo = 1
    alto = 100
    intentos = 0

    while bajo <= alto:
        medio = (bajo + alto) // 2
        intentos += 1
        print(f"Mi adivinanza es: {medio}")
        comentarios = input("¿Es (a)lto, (b)ajo o (c)orrecto? ").lower()

        if comentarios == 'c':
            print(f"¡Yay! Adiviné tu número en {intentos} intentos.")
            break
        elif comentarios == 'a':
            alto = medio - 1
        elif comentarios == 'b':
            bajo = medio + 1
        else:
            print("Por favor ingresa 'a', 'b' o 'c'.")

    if bajo > alto:
        print("Algo salió mal. ¿Estás seguro de que diste los comentarios correctos?")

juego_adivinanza()
