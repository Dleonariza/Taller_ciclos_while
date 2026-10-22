"""
Una actividad recibe números uno a uno hasta que aparezca -50. Muestre la suma de todas las
lecturas anteriores; -50 no forma parte de los datos y nunca se suma. Los demás valores, incluidos
negativos distintos de -50 y el cero, sí participan. Si el primer dato es -50, la suma es cero. El flujo siempre
contiene el centinela.
Fórmula o relación: Total = suma de las lecturas anteriores al primer -50.
"""

suma = 0
while True:
    num = int(input("Digite un numero: "))
    if num == -50:
        break
    suma += num
    

print("Suma: ", suma)