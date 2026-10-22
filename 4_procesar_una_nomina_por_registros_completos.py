"""
Una nómina ficticia recibe primero el salario mensual de un trabajador. Cero termina el registro y
no requiere otros datos. Un salario mensual positivo se acompaña de días trabajados, entero de 0 a 30,
bonos no negativos y otras deducciones no negativas. Muestre el pago neto de cada trabajador, en
orden de lectura. La retención es 5 % y el aporte de seguridad es 12 % del devengado. Se garantiza que
las otras deducciones no superan el devengado después de esos descuentos. El flujo termina con salario

mensual cero. El salario proporcional corresponde al salario mensual multiplicado por los días
trabajados y dividido entre 30. El devengado es ese salario proporcional más los bonos. Tanto la
retención como el aporte se calculan sobre ese mismo devengado: se descuentan en total 17 %, queda
el 83 % y después se restan las otras deducciones. Todos los importes usan la misma unidad monetaria.
Sin trabajadores, informe «Sin trabajadores».
Fórmula o relación: Salario proporcional = mensual × días / 30. Devengado = salario proporcional +
bonos. Neto = devengado × 0,83 - otras deducciones.
"""

neto = 0
bandera = False
while True:
    salario_mensual = int(input("Digite el salario mensual: "))

    if salario_mensual == 0:
        bandera = True
        break

    dias_trabajados = int(input("Digite los días trabajados: "))
    bonos = int(input("Digite el bono: "))
    otras_deducciones = int(input("Digite otras deducciones"))

    salario_proporcional = salario_mensual * dias_trabajados / 30
    devengado = salario_proporcional + bonos
    neto = devengado * 0.83 - otras_deducciones

if bandera and neto == 0:
    print("Sin trabajadores")
else:
    print("Neto: ", neto)