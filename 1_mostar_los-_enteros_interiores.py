"""
Una actividad recibe dos enteros A y B con A < B. Muestre, en orden ascendente, todos los enteros
estrictamente mayores que A y menores que B. Los extremos no se muestran. Si no hay enteros entre
ellos, informe «No hay enteros interiores».
Fórmula o relación: Cada entero consecutivo difiere del anterior en 1.
"""

a = int(input("Digite un valor entero para A: "))
b = int(input("Digite un valor entero para B: "))
entero_entre_a_y_b = a + 1

if entero_entre_a_y_b == b:
    print("No hay enteros interiores")
while entero_entre_a_y_b < b:
    print(entero_entre_a_y_b)
    entero_entre_a_y_b += 1
