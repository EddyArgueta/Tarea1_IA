def tabla_multiplicar():
    numero = int(input("Ingresa un número: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

tabla_multiplicar()