#Sumar Ventas por Productos
#Dado el siguiente diccionario:
# ventas = {
#    'Producto': ['A', 'B', 'A', 'C', 'B', 'A'],
#    'Cantidad': [10, 5, 7, 3, 2, 8] 
#}
# Agrupa las cantidades por productos y muesta la suma total de ventas por cada uno.

def ventas_por_producto(ventas):
    productos = ventas['Producto']
    cantidades = ventas['Cantidad']
    resumen = {}

    for i in range(len(productos)):
        producto = productos[i]
        cantidad = cantidades[i]
        if producto in resumen:
            resumen[producto] += cantidad
        else:
            resumen[producto] = cantidad

    return resumen


ventas = {
    'Producto': ['A', 'B', 'A', 'C', 'B', 'A'],
    'Cantidad': [10, 5, 7, 3, 2, 8]
}

resultado = ventas_por_producto(ventas)
print("Ventas por producto:", resultado)