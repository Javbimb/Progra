class Calculadora:
    def __init__(self):
        self.numero1 = 0.0
        self.numero2 = 0.0

    def insertar_numero1(self, num):
        self.numero1 = num

    def insertar_numero2(self, num):
        self.numero2 = num

    def obtener_suma(self):
        return self.numero1 + self.numero2

    def obtener_resta(self):
        return self.numero1 - self.numero2

    def obtener_multiplicacion(self):
        return self.numero1 * self.numero2

    def obtener_division(self):
        if self.numero2 != 0:
            return self.numero1 / self.numero2
        else:
            return "No se puede dividir por cero."


mi_calculadora = Calculadora()

while True:
    print("Menú:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elija una opción (1/2/3/4/5): ")

    if opcion == "1":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        mi_calculadora.insertar_numero1(num1)
        mi_calculadora.insertar_numero2(num2)
        resultado = mi_calculadora.obtener_suma()
        print("La suma es:", resultado)
    elif opcion == "2":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        mi_calculadora.insertar_numero1(num1)
        mi_calculadora.insertar_numero2(num2)
        resultado = mi_calculadora.obtener_resta()
        print("La resta es:", resultado)
    elif opcion == "3":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        mi_calculadora.insertar_numero1(num1)
        mi_calculadora.insertar_numero2(num2)
        resultado = mi_calculadora.obtener_multiplicacion()
        print("La multiplicación es:", resultado)
    elif opcion == "4":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        mi_calculadora.insertar_numero1(num1)
        mi_calculadora.insertar_numero2(num2)
        resultado = mi_calculadora.obtener_division()
        print("La división es:", resultado)
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida (1/2/3/4/5).")
