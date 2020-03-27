import tile
import random
import sys

def menu():
    print("***********************2048**********************")
    print("Emepezar nueva partida: 1")
    print("Empezar partida guardada: 2")
    print("Salir del juego: 3")
    select = int(input("Seleccione una opcion: "))
    if select == 3:
        print("Opcion 3")
        sys.exit(0)
    return select


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
            for m in range(mode - len(str(tiles[k][i].getValue()))):
                print(" ", end="")
            print(tiles[k][i].getValue(), end="")
        print("|")
    for j in range(size):
        print("+", end="")
        for k in range(mode):
            print("-", end="")
    print("+")


def randInt(val):
    rand = int(random.random() * val)
    return rand


def addValue(tiles):
    randVal = random.choices([1, 2], [0.75, 0.25])
    while True:
        randX = randInt(len(tiles))
        randY = randInt(len(tiles))
        if tiles[randX][randY].getValue() == " ":
            tiles[randX][randY].setValue(randVal[0])
            break
    return tiles


def setGrid(size, blocks):
    tiles = [[tile.Tile() for j in range(size)] for i in range(size)]
    for i in range(2):
        tiles = addValue(tiles)
        print("a")
    count = 0
    for i in range(blocks):
        while count <= i:
            randX = randInt(size)
            randY = randInt(size)
            if tiles[randX][randY].getValue() == " ":
                tiles[randX][randY].setValue("*")
                count += 1
    for i in range(len(tiles)):
        for j in range(len(tiles)):
            tiles[i][j].setMode(1)
    return tiles


def newGame():
    size = int(input("Introduzca el tamaño del tablero"))
    blocks = int(input("Introduzca el numero de obstaculos"))
    tiles = setGrid(size, blocks)
    board(size, 1, tiles)
    return size, 1, tiles


def movement(key, movTiles):
    if key == "W":
        print("Arriba")
        for i in range(len(movTiles)):
            for j in range(len(movTiles) - 1, 0, -1):
                for k in range(len(movTiles)):
                    if movTiles[k][j-1].getValue() == " " and movTiles[k][j].getValue() != "*":
                        movTiles[k][j-1].setValue(movTiles[k][j].getValue())
                        movTiles[k][j].setValue(" ")
                    elif movTiles[k][j - 1].getValue() == movTiles[k][j].getValue() and movTiles[k][j].getValue() != "*":
                        movTiles[k][j - 1].setValue(movTiles[k][j - 1].getValue() + movTiles[k][j].getValue())
                        movTiles[k][j].setValue(" ")
        return movTiles
    elif key == "A":
        print("Izquierda")
        for i in range(len(movTiles)):
            for j in range(len(movTiles)):
                for k in range(len(movTiles) - 1, 0, -1):
                    if movTiles[k - 1][j].getValue() == " " and movTiles[k][j].getValue() != "*":
                        movTiles[k - 1][j].setValue(movTiles[k][j].getValue())
                        movTiles[k][j].setValue(" ")
                    elif movTiles[k - 1][j].getValue() == movTiles[k][j].getValue() and movTiles[k][j].getValue() != "*":
                        movTiles[k - 1][j].setValue(movTiles[k - 1][j].getValue() + movTiles[k][j].getValue())
                        movTiles[k][j].setValue(" ")
        return movTiles
    elif key == "D":
        print("Derecha")
        for i in range(len(movTiles)):
            for j in range(len(movTiles)):
                for k in range(1, len(movTiles), 1):
                    if movTiles[k][j].getValue() == " " and movTiles[k - 1][j].getValue() != "*":
                        movTiles[k][j].setValue(movTiles[k - 1][j].getValue())
                        movTiles[k - 1][j].setValue(" ")
                    elif movTiles[k][j].getValue() == movTiles[k - 1][j].getValue() and movTiles[k - 1][j].getValue() != "*":
                        movTiles[k][j].setValue(movTiles[k][j].getValue() + movTiles[k - 1][j].getValue())
                        movTiles[k - 1][j].setValue(" ")
        return movTiles
    elif key == "S":
        print("Abajo")
        for i in range(len(movTiles)):
            for j in range(1, len(movTiles), 1):
                for k in range(len(movTiles)):
                    if movTiles[k][j].getValue() == " " and movTiles[k][j - 1].getValue() != "*":
                        movTiles[k][j].setValue(movTiles[k][j - 1].getValue())
                        movTiles[k][j - 1].setValue(" ")
                    elif movTiles[k][j].getValue() == movTiles[k][j - 1].getValue() and movTiles[k][j - 1].getValue() != "*":
                        movTiles[k][j].setValue(movTiles[k][j].getValue() + movTiles[k][j - 1].getValue())
                        movTiles[k][j - 1].setValue(" ")
        return movTiles


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
    board(size, mode, tiles)
    return tiles

while True:
    select = menu()

    if select == 1:
        print("Opcion 1")
        data = newGame()
        size = data[0]
        mode = data[1]
        tiles = data[2]
        while True:
            key = input("(W)Arriba, (A)Izquierda, (D)Derecha, (S)Abajo, (M)Modo, (G)Guardar, (F)Fin")
            if key == "W" or key == "A" or key == "D" or key == "S":
                tiles = movement(key, tiles)
                tiles = addValue(tiles)
                board(size, mode, tiles)
            elif key == "M":
                tiles = changeMode(tiles)
            elif key == "F":
                break

