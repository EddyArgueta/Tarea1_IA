#Escriba un programanque solicite ingresar el nombre de varios etudiantes y sus notas.
#Y lo almacena en un diccionario. Al final, nos muestra los datos almacenados.

def registrar_estudiante():
    estudiantes = {}
    cantidad = int(input("Cuantos estudiantes deseas registrar? "))

    for i in range(cantidad):
        nombre = input("Ingresa el nombre del estudiante: ")
        nota = float(input("Ingresa la nota: "))
        estudiantes[nombre] = nota

    print("Datos almacenados: ")
    print(estudiantes)

registrar_estudiante()
    