"""
Un curso recibe notas entre 0 y 100, una a una, hasta recibir -99. Muestre la cantidad de notas y
su promedio. El centinela no es una nota y no participa en el cálculo. Si aparece primero, muestre
cantidad cero y «Sin notas» en lugar de un promedio. El flujo siempre contiene -99. El promedio es la
suma de las notas aceptadas dividida entre su cantidad.
Fórmula o relación: Promedio = suma de las notas / cantidad de notas, solo cuando la cantidad sea
positiva.
"""

suma_notas = 0
promedio = 0
cantidad_notas = 0
while True:
    while True:
        nota = int(input("Digite una nota: "))
        if 0 <= nota <= 100 or nota == -99:
            break
        print("Nota invalida, digite nuevamente...")
    if nota == -99:
        break
    suma_notas += nota
    cantidad_notas += 1

if cantidad_notas == 0:
    print("Cantidad: ", 0, " Sin notas")
else:
    promedio = suma_notas / cantidad_notas
    print("Cantidad: ", cantidad_notas, " Promedio: ", promedio)