nlinea = int(input("Ingrese el número de línea: "))
precio_por_metro_cuadrado = float(input("Ingrese el precio de venta por metro cuadrado (Q): "))
metros_cuadrados_vendidos = float(input("Ingrese la cantidad de metros cuadrados vendidos al mes: "))
n_empleados = int(input("Ingrese el número de empleados: "))

costo_por_hora_empleado = []
horas_trabajadas = []

for i in range(n_empleados):
    costo_hora = float(input("Ingrese el costo (Q) por hora para el empleado " + str(i+1) +": "))
    horas = float(input("Ingrese la cantidad de horas trabajadas por el empleado " + str(i+1) + ": "))
    costo_por_hora_empleado.append(costo_hora)
    horas_trabajadas.append(horas)

print("        ")

print("Metros vendidos en linea 1: "+str(metros_cuadrados_vendidos))
print("Precio por mt2: "+ str(precio_por_metro_cuadrado))
print("Costo por metro cuadrado:")

for i in range(n_empleados):
    print("   Horas del empleado "+ str(i + 1) + ": " + str(horas_trabajadas[i]))
    print("   Precio por hora del empleado " + str(i + 1) + ": " + str(costo_por_hora_empleado[i]) + "Q")

print("  ")

ganancia_tot = precio_por_metro_cuadrado * metros_cuadrados_vendidos
print("Ganancia total = " + str(ganancia_tot))

costo_tot = sum(costo_por_hora_empleado[i] * horas_trabajadas[i] for i in range(n_empleados))
print("Costo total = " + str(costo_tot))

ganancia_neta = ganancia_tot - costo_tot
print("Ganancia neta = " + str(ganancia_neta))

eficiencia = ganancia_neta / n_empleados
print("La eficiencia de esta Linea fue de: "+ str(eficiencia))



print(" ")




nlinea2 = int(input("Ingrese el número de línea: "))
precio_por_metro_cuadrado2 = float(input("Ingrese el precio de venta por metro cuadrado (Q): "))
metros_cuadrados_vendidos2 = float(input("Ingrese la cantidad de metros cuadrados vendidos al mes: "))
n_empleados2 = int(input("Ingrese el número de empleados: "))

costo_por_hora_empleado2 = []
horas_trabajadas2 = []

for i in range(n_empleados2):
    costo_hora2 = float(input("Ingrese el costo (Q) por hora para el empleado " + str(i+1) +": "))
    horas2 = float(input("Ingrese la cantidad de horas trabajadas por el empleado " + str(i+1) + ": "))
    costo_por_hora_empleado2.append(costo_hora2)
    horas_trabajadas2.append(horas2)

print("        ")

print("Metros vendidos en linea 1: "+str(metros_cuadrados_vendidos2))
print("Precio por mt2: "+ str(precio_por_metro_cuadrado2))
print("Costo por metro cuadrado:")

for i in range(n_empleados2):
    print("   Horas del empleado "+ str(i + 1) + ": " + str(horas_trabajadas2[i]))
    print("   Precio por hora del empleado " + str(i + 1) + ": " + str(costo_por_hora_empleado2[i]) + "Q")

print("  ")

ganancia_tot2 = precio_por_metro_cuadrado2 * metros_cuadrados_vendidos2
print("Ganancia total = " + str(ganancia_tot2))

costo_tot2 = sum(costo_por_hora_empleado2[i] * horas_trabajadas2[i] for i in range(n_empleados2))
print("Costo total = " + str(costo_tot2))

ganancia_neta2 = ganancia_tot2 - costo_tot2
print("Ganancia neta = " + str(ganancia_neta2))

eficiencia2 = ganancia_neta2 / n_empleados2
print("La eficiencia de esta Linea fue de: "+ str(eficiencia2))



if eficiencia > eficiencia2:
    print("La linea 1 es mayor eficiente")

elif eficiencia < eficiencia2:
    print("La linea 2 es mayor eficiente")

elif eficiencia == eficiencia2:
    print("Ambas lineas son igual de eficientes")