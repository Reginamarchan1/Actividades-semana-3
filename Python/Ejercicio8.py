def generar_palindromo(cadena):
    cadena.lower()
    cadena = ''.join(caracter for caracter in cadena if caracter.isalnum())
    return cadena == cadena[::-1]

print(generar_palindromo("oso"))

print("Fin.")