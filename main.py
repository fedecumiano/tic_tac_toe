# Se le pide al jugador 1 elegir X ó O
def elegir_pieza():
    jug1 = input("Jugador 1 Elije (X/O): ")
    while jug1.upper() != "X" and jug1.upper() != "O":
        jug1 = input("Eleccion invalida, Debe elegir (X/O): ")
    jug1 = jug1.upper()
    jug2 = "O" if jug1 == "X" else "X"
    return jug1, jug2



def ganador(t):
    g = None
    for i in range(3):
        # checkea ganador en filas
        if t[i][0] == t[i][1] == t[i][2]:
            g = t[i][0]
            break
        # checkea ganador en columnas
        if t[0][i] == t[1][i] == t[2][i]:
            g = t[0][i]
            break
    # checkea ganador en diagonal
    if t[0][0] == t[1][1] == t[2][2] or t[0][2] == t[1][1] == t[2][0]:
        g = t[1][1]
    return g if g != "-" else None


def agregar_pieza(jugador, posicion, tablero):
    tablero[posicion[0]][posicion[1]] = jugador


def posicion_libre(pos, tablero):
    return tablero[pos[0]][pos[1]] not in {"X", "O"}


def coordenadas(pos):
    if 1 <= pos <= 9:
        pos = pos - 1
        fila = pos // 3
        columna = pos % 3
        return fila, columna
    raise ValueError(f"Pos {pos} is not valid")


def tablero_lleno(tablero):
    for i in range(1,10):
        p, q = coordenadas(i)
        if tablero[p][q] not in {"X", "O"}:
            return False
    return True


def mostrar(tablero):
    for i in range(3):
        print(f"  {tablero[i][0]}  |  {tablero[i][1]}  |  {tablero[i][2]}")
        print("-" * 22)


def juego():
    tablero = [["-" for _ in range(3)] for _ in range(3)]
    mostrar(tablero)
    jug1, jug2 = elegir_pieza()
    print(f"Jugador 1 eligió: '{jug1}' \n Jugador 2 eligió '{jug2}'")
    while not ganador(tablero) and not tablero_lleno(tablero):
        pos = -1
        while pos not in range(1, 10):
            mostrar(tablero)
            try:
                pos = int(input("Ingrese un numero no ocupado entre 1 y 9 (Jugador 1): "))
                if not posicion_libre(coordenadas(pos), tablero):
                    pos = -1
            except ValueError:
                print("Valor no aceptado")
        pos = coordenadas(pos)
        agregar_pieza(jug1, pos, tablero)
        if ganador(tablero) == jug1 or tablero_lleno(tablero):
            break
        pos = -1
        while pos not in range(1, 10):
            mostrar(tablero)
            try:
                pos = int(input("Ingrese un numero no ocupado entre 1 y 9 (Jugador 2): "))
                if not posicion_libre(coordenadas(pos), tablero):
                    pos = -1
            except ValueError:
                print("Valor no aceptado")
        pos = coordenadas(pos)
        agregar_pieza(jug2, pos, tablero)
    mostrar(tablero)
    print("Ganador: " + ganador(tablero))


juego()
