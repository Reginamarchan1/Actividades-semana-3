def bisiesto(año):
    return año % 4 == 0 and año % 100 != 0 or (año % 400 == 0)

print(bisiesto(2006))

print("Fin.")