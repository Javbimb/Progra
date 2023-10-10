def obtener_hexadecimal(valor):
    valor = str(valor)
    n_l = {
        "10": "A",
        "11": "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F",
    }
    if valor in n_l:
        return n_l[valor]
    else:
        return valor


def decimal_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        residuo = decimal % 16
        x = obtener_hexadecimal(residuo)
        hexadecimal = x + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal

decimal = int(
    input("Escribe un número: "))
hexadecimal = decimal_hexadecimal(decimal)
print("El decimal " + str(decimal)+ " es " + str(hexadecimal) + " en hexadecimal")