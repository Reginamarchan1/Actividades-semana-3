def maximo_divisor(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

print(maximo_divisor(56, 98))

print("Fin.")
    