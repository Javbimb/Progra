#José Andrés Puaque Guerra #1189523
#Erick Javier Wolhers Estrada #1128723
print("Ejercicio de clases")

Nombre = input("Ingrese su nombre: ")
Apellido = input("Ingrese su apellido: ")
ACasada = input("Ingrese su apellido de casada (Si no tiene coloque 0): ")
fecha = input("Ingrese su fecha de nacimiento: ")
class persona:
    def __init__(Self, Nombre, Apellido, ACasada, fecha):
        Self.Nombre = Nombre
        Self.Apellido = Apellido
        Self.Acasada = ACasada
        Self.fecha = fecha
Persona1 = persona(Nombre, Apellido, ACasada, fecha)

print ("Nombre:", Persona1.Nombre)
print ("Apellido:", Persona1.Apellido)
if ACasada != str(0):
    print ("Apellido de casada:", Persona1.Acasada)
    print ("Fecha de nacimiento:", Persona1.fecha)
    print ("Nombre completo:", Persona1.Nombre,  Persona1.Apellido,  "de",  Persona1.Acasada)