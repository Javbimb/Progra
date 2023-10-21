cadena = input("Ingresa una cadena de caracteres: ")
contador_0 = 0
contador_1 = 0
contador_otros = 0
for caracter in cadena:
    if caracter == '0':
        contador_0 += 1
    elif caracter == '1':
        contador_1 += 1
    else:
        contador_otros += 1
print(f"Cadena: {cadena}")
print(f"Cantidad 0: {contador_0}")
print(f"Cantidad 1: {contador_1}")
print(f"Otros caracteres: {contador_otros}")




