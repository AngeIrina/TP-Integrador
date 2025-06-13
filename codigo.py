# Parte B: Operaciones con años de nacimiento

#Programacion A

# Ingreso de DNIs reales o ficticios
dnis = [
    "44606468",  # Persona A
    "43150956",  # Persona B
    "42533594"   # Persona C
]

# Generacion de conjuntos de digitos unicos mediante set()
conjuntos = []
for dni in dnis:
    conjuntos.append(set(dni))

# Mostrar conjuntos generados previamente, convirtiendo conjuntos en int
print("Conjuntos generados a partir de los DNIs:")
for i, conjunto in enumerate(conjuntos):
    print(f"Conjunto {chr(65+i)} = {set(map(int, conjunto))}")

# Calculo de operaciones entre conjuntos
# Renombra conjuntos como A, B y C como INT
A, B, C = conjuntos
A = set(map(int, A))
B = set(map(int, B))
C = set(map(int, C))

print("\nOperaciones entre conjuntos:")
print("Union A ∪ B:", A.union(B))
print("Interseccion A ∩ B:", A.intersection(B))
print("Diferencia A - B:", A.difference(B))
print("Diferencia simetrica A Δ B:", A.symmetric_difference(B))

# Conteo de frecuencia de cada digito en cada DNI
print("\nFrecuencia de digitos en cada DNI:")
for i, dni in enumerate(dnis):
    frecuencia = {}
    for digito in dni:
        frecuencia[digito] = frecuencia.get(digito, 0) + 1
    print(f"DNI {chr(65+i)}: {frecuencia}")

# Suma total de los digitos de cada DNI
print("\nSuma total de los digitos de cada DNI:")
for i, dni in enumerate(dnis):
    suma = sum(map(int, dni))
    print(f"Suma de DNI {chr(65+i)}: {suma}")

# Evaluacion de condiciones logicas

# Condicion 1: Digito compartido (interseccion entre todos los conjuntos)
digitos_comunes = A & B & C 
if digitos_comunes:
    print("\nDigitos compartidos:", digitos_comunes)

# Condicion 2: Diversidad numerica alta (algun conjunto con mas de 6 elementos)
for i, conjunto in enumerate([A, B, C]):
    if len(conjunto) > 6:
        print(f"Conjunto {chr(65+i)}: Diversidad numerica alta")




#Programacion B

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


