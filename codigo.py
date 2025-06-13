# Operaciones con años de nacimiento
# Ingreso de los años de nacimiento (Si dos o mas integrantes del grupo tienen el mismo año, ingresar algún dato ficticio, según el caso).

# Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas.

# Si todos nacieron después del 2000, mostrar "Grupo Z".

# Si alguno nació en año bisiesto, mostrar "Tenemos un año especial".

# Implementar una función para determinar si un año es bisiesto.

# Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales.

# def es_bisiesto(anio):
#     """Determina si un año es bisiesto."""
#     if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
#         return True
#     return False

# def producto_cartesiano(anios, edades):
#     """Calcula el producto cartesiano entre dos conjuntos."""
#     return [(anio, edad) for anio in anios for edad in edades]

# def main():
#     anios = []
#     edades = []

#     # Ingreso de años de nacimiento
#     while True:
#         anio = input("Ingrese un año de nacimiento (o 'x' para terminar): ")
#         if anio.lower() == 'x':
#             break
#         try:
#             anio = int(anio)
#             anios.append(anio)
#         except ValueError:
#             print("Por favor, ingrese un año válido.")

#     # Ingreso de edades actuales
#     while True:
#         edad = input("Ingrese una edad actual (o 'x' para terminar): ")
#         if edad.lower() == 'x':
#             break
#         try:
#             edad = int(edad)
#             edades.append(edad)
#         except ValueError:
#             print("Por favor, ingrese una edad válida.")

#     # Contar años pares e impares
#     pares = sum(1 for anio in anios if anio % 2 == 0)
#     impares = len(anios) - pares

#     print(f"Nacieron {pares} en años pares y {impares} en años impares.")

#     # Verificar si todos nacieron después del 2000
#     if all(anio > 2000 for anio in anios):
#         print("Grupo Z")

#     # Verificar si hay algún año bisiesto
#     if any(es_bisiesto(anio) for anio in anios):
#         print("Tenemos un año especial")

#     # Calcular el producto cartesiano
#     producto = producto_cartesiano(anios, edades)
#     print("Producto cartesiano entre años y edades:", producto)



def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def producto_cartesiano(anios, edades):
    return [(anio, edad) for anio in anios for edad in edades]

def cargar_lista(mensaje):
    lista = []
    while True:
        valor = input(mensaje)
        if valor.lower() == 'x':
            break
        try:
            valor = int(valor)
            if "año" in mensaje and valor in lista:
                print("Ese año ya fue ingresado. Use un dato ficticio si es necesario.")
                continue
            lista.append(valor)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    return lista

def main():
    anios = cargar_lista("Ingrese un año de nacimiento (o 'x' para terminar): ")
    if not anios:
        print("No se ingresaron años de nacimiento. El programa terminará.")
        return
    
    edades = cargar_lista("Ingrese una edad actual (o 'x' para terminar): ")
    if not edades:
        print("No se ingresaron edades. El programa terminará.")
        return

    if len(anios) != len(edades):
        print("Advertencia: la cantidad de años y edades no coincide.")

    pares = 0
    impares = 0

    for anio in anios:
        if anio % 2 == 0:
            pares += 1
        else:
            impares += 1

    print(f"\nNacieron {pares} en años pares y {impares} en años impares.")

    if all(anio > 2000 for anio in anios):
        print("Grupo Z")

    if any(es_bisiesto(anio) for anio in anios):
        print("Tenemos un año especial")

    producto = producto_cartesiano(anios, edades)
    print("\nProducto cartesiano entre años y edades:")
    for par in producto:
        print(par)

    print("\nResumen:")
    print(f"- Años: {anios}")
    print(f"- Edades: {edades}")

main()


