import random

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

def verificar_ganador(tablero):
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != ' ':
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != ' ':
            return tablero[0][i]

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
        return tablero[0][2]

    return None

def tablero_lleno(tablero):
    for fila in tablero:
        if ' ' in fila:
            return False
    return True

def movimiento_valido(fila, columna, tablero):
    return 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == ' '

def realizar_movimiento(fila, columna, jugador, tablero):
    tablero[fila][columna] = jugador

def obtener_movimiento_minimax(tablero, jugador):
    if jugador == 'X':
        eval, movimiento = minimax(tablero, jugador)
    else:
        eval, movimiento = minimax(tablero, jugador, maximizing_player=False)
    return movimiento

def minimax(tablero, jugador, maximizing_player=True):
    ganador = verificar_ganador(tablero)
    if ganador:
        return 1 if ganador == 'X' else -1, None
    if tablero_lleno(tablero):
        return 0, None

    if maximizing_player:
        max_eval = float('-inf')
        mejor_movimiento = None
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == ' ':
                    tablero[i][j] = jugador
                    eval, _ = minimax(tablero, jugador, False)
                    tablero[i][j] = ' '
                    if eval > max_eval:
                        max_eval = eval
                        mejor_movimiento = (i, j)
        return max_eval, mejor_movimiento
    else:
        min_eval = float('inf')
        peor_movimiento = None
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == ' ':
                    tablero[i][j] = 'O' if jugador == 'X' else 'X'
                    eval, _ = minimax(tablero, jugador, True)
                    tablero[i][j] = ' '
                    if eval < min_eval:
                        min_eval = eval
                        peor_movimiento = (i, j)
        return min_eval, peor_movimiento

def jugar_tic_tac_toe():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    jugador_actual = 'X'
    ganador = None

    while not (tablero_lleno(tablero) or ganador):
        imprimir_tablero(tablero)
        print("Tablero")
        if jugador_actual == 'X':
            fila = int(input("Ingrese la fila (0, 1, 2): "))
            columna = int(input("Ingrese la columna (0, 1, 2): "))
            if not movimiento_valido(fila, columna, tablero):
                print("Movimiento no válido. Intente de nuevo.")
                continue
        else:
            fila, columna = obtener_movimiento_minimax(tablero, jugador_actual)

        realizar_movimiento(fila, columna, jugador_actual, tablero)
        ganador = verificar_ganador(tablero)

        jugador_actual = 'O' if jugador_actual == 'X' else 'X'

    imprimir_tablero(tablero)

    if ganador:
        print(f"¡El jugador {ganador} ha ganado!")
    else:
        print("¡Empate!")

if __name__ == "__main__":
    jugar_tic_tac_toe()
