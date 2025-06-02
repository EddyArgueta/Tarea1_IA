def buscar_numero_mayor(lista):
    mayor = lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor

# Ejemplo de uso:
numeros = [2, 29, 44, 10, 17]
print("El número mayor es:", buscar_numero_mayor(numeros))