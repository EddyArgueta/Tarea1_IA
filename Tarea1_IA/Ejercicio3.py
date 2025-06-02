#Ejercicio 3: Cree un programa que elimine los elementos repetidos de una lista y 
#devuelva una nueva lista con elementos unicos ordenados
def eliminar_elementos_repetidos(lista):
    lista_unica = sorted(set(lista)) #Return a new list containing all items from the iterable in ascending order.
    return lista_unica

# Ejemplo de uso:
entrada = [4, 3, 7, 4, 2, 1, 9, 7, 9, 4, 3]
resultado = eliminar_elementos_repetidos(entrada)
print("La nueva lista con elementos unicos ordenados es:", resultado)