def es_palindromo(cadena):
    cadena = cadena.replace(" "," ") # Reemplaza " ".
    cadena = cadena.lower() # Hace todo minuscula. 
    cadena2 = " "
    n = len(cadena)
    # El for recorre de forma inversa cadena.
    for i in range(n-1, -1, -1):
        cadena2 += cadena[i] # Concatenamos la letra.
    return cadena == cadena2 # Comparamos si son iguales.

resultado = es_palindromo("Anita lava la tina")
print("¿Es palindromo?", resultado)

print("Fin.")    