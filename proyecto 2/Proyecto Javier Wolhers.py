import random

def inicializar_tablero():
    return [[' ' for _ in range(10)] for _ in range(10)]

def imprimir_tablero(tablero):
    letras = 'ABCDEFGHIJ'
    print("   1 2 3 4 5 6 7 8 9 10")
    print("  ---------------------")
    for i in range(10):
        print(f"{letras[i]} |{'|'.join(tablero[i])}|")

def colocar_barco(tablero, fila, columna, tamano, orientacion):
    if orientacion == 'horizontal':
        for i in range(tamano):
            tablero[fila][columna + i] = 'O'
    elif orientacion == 'vertical':
        for i in range(tamano):
            tablero[fila + i][columna] = 'O'

def disparar(tablero, fila, columna, barcos_hundidos):
    if tablero[fila][columna] == 'O':
        print("¡Impacto! Has alcanzado un barco.")
        tablero[fila][columna] = 'X'
        if verificar_hundido(tablero, fila, columna):
            print("¡Hundiste un barco!")
            barcos_hundidos.append((fila, columna))
    else:
        print("¡Fallo! No hay ningún barco en esta casilla.")

def verificar_hundido(tablero, fila, columna):
    tamano_barco = 0
    if tablero[fila][columna] == 'O':
        while columna + tamano_barco < 10 and tablero[fila][columna + tamano_barco] == 'O':
            tamano_barco += 1
        while fila + tamano_barco < 10 and tablero[fila + tamano_barco][columna] == 'O':
            tamano_barco += 1
        return tamano_barco == 3 or tamano_barco == 5
    return False

def verificar_ganador(barcos_hundidos):
    return len(barcos_hundidos) == 5

def determinar_ganador(turno_actual):
    if turno_actual == 1:
        return "Jugador 1"
    else:
        return "Jugador 2"

def juego_batalla_naval():
    tablero_jugador1 = inicializar_tablero()
    tablero_jugador2 = inicializar_tablero()
    barcos_hundidos_jugador1 = []
    barcos_hundidos_jugador2 = []

    print("¡Bienvenido a Batalla Naval!")

    print("\nJugador 1, coloca tus barcos:")
    colocar_barcos(tablero_jugador1)

    print("\nJugador 2, coloca tus barcos:")
    colocar_barcos(tablero_jugador2)

    turno_actual = 1
    while True:
        if turno_actual == 1:
            print("\nJugador 1, es tu turno:")
            imprimir_tablero(tablero_jugador2)
            disparo_jugador1 = pedir_disparo()
            disparar(tablero_jugador2, *disparo_jugador1, barcos_hundidos_jugador2)
            if verificar_ganador(barcos_hundidos_jugador2):
                print(f"¡Felicidades! {determinar_ganador(turno_actual)} es el ganador.")
                break
            turno_actual = 2
        else:
            print("\nJugador 2, es tu turno:")
            imprimir_tablero(tablero_jugador1)
            disparo_jugador2 = pedir_disparo()
            disparar(tablero_jugador1, *disparo_jugador2, barcos_hundidos_jugador1)
            if verificar_ganador(barcos_hundidos_jugador1):
                print(f"¡Felicidades! {determinar_ganador(turno_actual)} es el ganador.")
                break
            turno_actual = 1

    print("\nEl juego ha terminado.")

def colocar_barcos(tablero):
    for _ in range(3):
        colocar_barco_manual(tablero, 3)
    for _ in range(2):
        colocar_barco_manual(tablero, 5)

def colocar_barco_manual(tablero, tamano):
    imprimir_tablero(tablero)
    fila, columna, orientacion = pedir_coordenadas(tamano)
    while not validar_coordenadas(tablero, fila, columna, tamano, orientacion):
        print("¡Posición inválida! Inténtalo de nuevo.")
        fila, columna, orientacion = pedir_coordenadas(tamano)
    colocar_barco(tablero, fila, columna, tamano, orientacion)

def pedir_coordenadas(tamano):
    letras_validas = 'ABCDEFGHIJ'
    fila = input(f"Ingrese la letra de la fila (A-J): ").upper()
    while fila not in letras_validas:
        fila = input("¡Letra inválida! Ingrese la letra de la fila (A-J): ").upper()
    columna = input(f"Ingrese el número de la columna (1-10): ")
    while not columna.isdigit() or not (1 <= int(columna) <= 10):
        columna = input("¡Número inválido! Ingrese el número de la columna (1-10): ")
    orientacion = input("Ingrese la orientación del barco (horizontal/vertical): ").lower()
    while orientacion not in ['horizontal', 'vertical']:
        orientacion = input("¡Orientación inválida! Ingrese la orientación del barco (horizontal/vertical): ")
    return letras_validas.index(fila), int(columna) - 1, orientacion

def validar_coordenadas(tablero, fila, columna, tamano, orientacion):
    if orientacion == 'horizontal':
        return all(tablero[fila][columna + i] == ' ' for i in range(tamano))
    elif orientacion == 'vertical':
        return all(tablero[fila + i][columna] == ' ' for i in range(tamano))

def pedir_disparo():
    letras_validas = 'ABCDEFGHIJ'
    fila = input(f"Ingrese la letra de la fila a disparar (A-J): ").upper()
    while fila not in letras_validas:
        fila = input("¡Letra inválida! Ingrese la letra de la fila a disparar (A-J): ").upper()
    columna = input(f"Ingrese el número de la columna a disparar (1-10): ")
    while not columna.isdigit() or not (1 <= int(columna) <= 10):
        columna = input("¡Número inválido! Ingrese el número de la columna a disparar (1-10): ")
    return letras_validas.index(fila), int(columna) - 1

juego_batalla_naval()
