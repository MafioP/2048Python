import tile
import random
import sys
import window


'''Menu principal del juego, devuelve la seleccion del usuario'''
def menu():
    print("***********************2048**********************")
    print("Empezar nueva partida: 1")
    print("Empezar partida guardada: 2")
    print("Salir del juego: 3")
    select = int(input("Seleccione una opcion: "))
    return select


'''Imprime el tablero dado un tamaño, modo de juego y la matriz de valores'''
def board(size, mode, tiles):
    if mode == 3:
        mode += 1
    for i in range(size):
        print("+", end="")
        for j in range(size):
            for l in range(mode):
                print("-", end="")
            print("+", end="")
        print("")
        for k in range(size):
            print("|", end="")
            for m in range(mode - len(str(tiles[k][i].getDisplayValue()))):
                print(" ", end="")
            print(tiles[k][i].getDisplayValue(), end="")
        print("|")
    for j in range(size):
        print("+", end="")
        for k in range(mode):
            print("-", end="")
    print("+")


'''Devuelve un valor entero aleatorio'''
def randInt(val):
    rand = int(random.random() * val)
    return rand


'''Añade un valor al tablero con un 75% de ser 1 y 25% de ser 2'''
def addValue(tiles):
    randVal = random.choices([1, 2], [0.75, 0.25])
    while True:
        randX = randInt(len(tiles))
        randY = randInt(len(tiles))
        if tiles[randX][randY].getValue() == " ":
            tiles[randX][randY].setValue(randVal[0])
            break
    return tiles


'''Inicializa el tablero, estableciendo los 2 valores iniciales y los obstaculos, aparte de la matriz de valores'''
def setGrid(size, blocks):
    tiles = [[tile.Tile() for j in range(size)] for i in range(size)]
    for i in range(2):
        tiles = addValue(tiles)
    count = 0
    for i in range(blocks):
        while count <= i:
            randX = randInt(size)
            randY = randInt(size)
            if tiles[randX][randY].getValue() == " ":
                tiles[randX][randY].setValue("*")
                count += 1
    return tiles


'''Al empezar una nueva partida esta funcion pide el tamaño y los obstaculos, la inicializa y la escribe en consola'''
def newGame():
    size = int(input("Introduzca el tamaño del tablero"))
    blocks = int(input("Introduzca el numero de obstaculos"))
    tiles = setGrid(size, blocks)
    board(size, 1, tiles)
    return size, 1, tiles


'''Se encarga de mover las casillas y de sumarlas cuando sea posible. Cuando se suman dos casillas, la que incrementa la cifra se bloquea
para evitar que se sume mas de una vez en la misma casilla'''
def movement(key, score, tiles):
    if key == "W":
        print("Arriba")
        for i in range(len(tiles)):
            for k in range(len(tiles)):
                for j in range(1, len(tiles), 1):
                    if tiles[k][j - 1].getValue() == " " and tiles[k][j].getValue() != "*":
                        tiles[k][j - 1].setValue(tiles[k][j].getValue())
                        tiles[k][j].setValue(" ")
                    elif tiles[k][j - 1].getValue() == tiles[k][j].getValue() and tiles[k][j].getValue() != "*":
                        if not tiles[k][j - 1].isLocked() and not tiles[k][j].isLocked():
                            tiles[k][j - 1].lock()
                            tiles[k][j - 1].setValue(tiles[k][j - 1].getValue() + 1)
                            tiles[k][j].setValue(" ")
                            score += 1

        return tiles, score
    elif key == "A":
        print("Izquierda")
        for i in range(len(tiles)):
            for j in range(len(tiles)):
                for k in range(1, len(tiles), 1):
                    if tiles[k - 1][j].getValue() == " " and tiles[k][j].getValue() != "*":
                        tiles[k - 1][j].setValue(tiles[k][j].getValue())
                        tiles[k][j].setValue(" ")
                    elif tiles[k - 1][j].getValue() == tiles[k][j].getValue() and tiles[k][j].getValue() != "*":
                        if not tiles[k - 1][j].isLocked() and not tiles[k][j].isLocked():
                            tiles[k - 1][j].lock()
                            tiles[k - 1][j].setValue(tiles[k - 1][j].getValue() + 1)
                            tiles[k][j].setValue(" ")
                            score += 1

        return tiles, score
    elif key == "D":
        print("Derecha")
        for i in range(len(tiles)):
            for j in range(len(tiles)):
                for k in range(len(tiles) - 1, 0, -1):
                    if tiles[k][j].getValue() == " " and tiles[k - 1][j].getValue() != "*":
                        tiles[k][j].setValue(tiles[k - 1][j].getValue())
                        tiles[k - 1][j].setValue(" ")
                    elif tiles[k][j].getValue() == tiles[k - 1][j].getValue() and tiles[k - 1][j].getValue() != "*":
                        if not tiles[k][j].isLocked() and not tiles[k - 1][j].isLocked():
                            print(tiles[k][j].isLocked())
                            tiles[k][j].lock()
                            print(tiles[k][j].isLocked())
                            tiles[k][j].setValue(tiles[k][j].getValue() + 1)
                            tiles[k - 1][j].setValue(" ")
                            score += 1

        return tiles, score
    elif key == "S":
        print("Abajo")
        for i in range(len(tiles)):
            for k in range(len(tiles)):
                for j in range(len(tiles) - 1, 0, -1):
                    if tiles[k][j].getValue() == " " and tiles[k][j - 1].getValue() != "*":
                        tiles[k][j].setValue(tiles[k][j - 1].getValue())
                        tiles[k][j - 1].setValue(" ")
                    elif tiles[k][j].getValue() == tiles[k][j - 1].getValue() and tiles[k][j - 1].getValue() != "*":
                        if not tiles[k][j].isLocked() and not tiles[k][j - 1].isLocked():
                            tiles[k][j].lock()
                            tiles[k][j].setValue(tiles[k][j].getValue() + 1)
                            tiles[k][j - 1].setValue(" ")
                            score += 1

        return tiles, score


'''Desbloquea todas las casillas para que se puedan volver a sumar'''
def unlockAll(tiles):
    for i in range(len(tiles)):
        for j in range(len(tiles)):
            tiles[j][i].unlock()
    return tiles


'''Pide el nuevo modo de juego y lo cambia acordemente'''
def changeMode(tiles):
    print("*******Seleccion de modo de juego********")
    print("Modo 1: Alfabeto")
    print("Modo 2: Nivel")
    print("Modo 3: 1024")
    print("Modo 4: 2048")
    mode = int(input("Escoja opcion:"))
    for i in range(len(tiles)):
        for j in range(len(tiles)):
            tiles[i][j].setMode(mode)
    board(len(tiles), mode, tiles)
    return mode


'''Lee el archivo donde esta guardada la partida'''
def readFile():
    fileName = input("Introduzca el nombre del fichero a leer")
    f = open(fileName, "r")
    score = int(f.readline())
    moves = int(f.readline())
    strSize = f.readline()
    tiles = [[tile.Tile() for j in range(len(strSize) - 1)] for i in range(len(strSize) - 1)]
    mode1Dic = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K" : 11}
    f.seek(len(str(score)) + len(str(moves)) + 4)           #ir a la posicion 0,0 de la matriz
    for i in range(len(tiles)):
        line = f.readline()
        for j in range(len(tiles)):
            if line[j] == ".":
                tiles[j][i].setValue(" ")
            elif line[j] == "*":
                tiles[j][i].setValue("*")
            else:
                tiles[j][i].setValue(mode1Dic[line[j]])
    f.close()

    return score, moves, tiles


'''Guarda la partida en un archivo existente o crea uno nuevo'''
def saveFile(score, moves, tiles):
    fileName = input("Introduzca el nombre del fichero a guardar")
    f = open(fileName, "w")
    f.write(str(score))
    f.write("\n")
    f.write(str(moves))

    for i in range(len(tiles)):
        f.write("\n")
        for j in range(len(tiles)):
            tiles[j][i].setMode(1)
            if tiles[j][i].getDisplayValue() == " ":
                f.write(".")
            else:
                f.write(tiles[j][i].getDisplayValue())
    f.close()


'''Comprueba si el tablero esta lleno y acaba el juego cuando se da el caso'''
def checkFullGrid(tiles):
    for i in range(len(tiles)):
        for j in range(len(tiles)):
            if tiles[j][i].getValue() == " ":
                return False
    return True


'''Comprueba si el jugador ha llegado al maximo nivel'''
def check2048(tiles):
    for i in range(len(tiles)):
        for j in range(len(tiles)):
            if tiles[j][i].getValue() == 11:
                return True
    return False


'''Metodo que corre el juego, controlando las entradas del jugador y llamando a las funciones correspondientes'''
def playGame(mode, score, moves, tiles):
    while True:
        key = input("(W)Arriba, (A)Izquierda, (D)Derecha, (S)Abajo, (M)Modo, (G)Guardar, (F)Fin")
        if key == "W" or key == "A" or key == "D" or key == "S":
            tiles, score = movement(key, score, tiles)
            tiles = unlockAll(tiles)
            addValue(tiles)
            board(len(tiles), mode, tiles)
            if check2048(tiles):
                print("HAS LLEGADO A 2048, ENHORABUENA HAS GANADO")
                print("PUNTUACION FINAL:", score, "|MOVIMIENTOS TOTALES:", moves)
                break
            if checkFullGrid(tiles):
                print("SE HA LLENADO EL TABLERO, HAS PERDIDO")
                print("PUNTUACION FINAL:", score, "|MOVIMIENTOS TOTALES:", moves)
                break
            else:
                moves +=1
                print("PUNTUACION:", score, " | ", " MOVIMIENTOS:", moves)

        elif key == "M":
            mode = changeMode(tiles)
        elif key == "G":
            saveFile(score, moves, tiles)
            print("GUARDANDO PARTIDA")
            break
        elif key == "F":
            break

'''Bucle principal del juego, que se repite hasta que el jugador sale de este usando la opcion 3 del menu'''

#
# while True:
#
#
#     select = menu()
#     score = 0
#     mode = 1
#     moves = 0
#     if select == 1:
#         print("Opcion 1")
#         data = newGame()
#         size = data[0]
#         mode = data[1]
#         tiles = data[2]
#         app = window.Window(0)
#         app.main_Frame.addData(5, 6)
#         app.MainLoop()
#         playGame(mode, score, moves, tiles)
#
#     if select == 2:
#         score, moves, tiles = readFile()
#         board(len(tiles), mode, tiles)
#         playGame(mode, score, moves, tiles)
#
#     if select == 3:
#         print("Opcion 3")
#         sys.exit(0)
