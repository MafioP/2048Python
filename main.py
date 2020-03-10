import tile
import random


def menu():
    print("***********************2048**********************")
    print("Emepezar nueva partida: 1")
    print("Empezar partida guardada: 2")
    print("Salir del juego: 3")
    select = int(input("Seleccione una opcion: "))
    return select


def board(size, mode, tiles):
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


def setGrid(size, blocks):
    tiles = [[tile.Tile() for j in range(size)] for i in range(size)]
    tiles[randInt(size)][randInt(size)].setValue(1)
    tiles[randInt(size)][randInt(size)].setValue(2)
    count = 0
    for i in range(blocks):
        while count <= i:
            randX = randInt(size)
            randY = randInt(size)
            if tiles[randX][randY].getValue() == " ":
                tiles[randX][randY].setValue("*")
                count += 1
                print(count)
    return tiles


def newGame():
    size = int(input("Introduzca el tamaño del tablero"))
    blocks = int(input("Introduzca el numero de obstaculos"))
    mode = int(input("Introduzca el modo de juego"))
    tiles = setGrid(size, blocks)
    board(size, mode, tiles)
    return size, mode, tiles


def movement(key, tiles):
    if key == "W":
        print("Arriba")
        for i in range(len(tiles)):
            for j in range(len(tiles)-1, 0, -1):
                for k in range(len(tiles)):
                    if tiles[k][j-1].getValue() == " "  and tiles[k][j].getValue() != "*":
                        tiles[k][j-1].setValue(tiles[k][j].getValue())
                        tiles[k][j].setValue(" ")
        return tiles
    elif key == "A":
        print("Izquierda")
        for i in range(len(tiles)):
            for j in range(len(tiles)):
                for k in range(len(tiles)-1, 0, -1):
                    if tiles[k-1][j].getValue() == " " and tiles[k][j].getValue() != "*":
                        tiles[k-1][j].setValue(tiles[k][j].getValue())
                        tiles[k][j].setValue(" ")
        return tiles
    elif key == "D":
        print("Derecha")
        for i in range(len(tiles)):
            for j in range(len(tiles)):
                for k in range(1, len(tiles), 1):
                    if tiles[k][j].getValue() == " " and tiles[k-1][j].getValue() != "*":
                        tiles[k][j].setValue(tiles[k-1][j].getValue())
                        tiles[k - 1][j].setValue(" ")
        return tiles
    elif key == "S":
        print("Abajo")
        for i in range(len(tiles)):
            for j in range(1, len(tiles), 1):
                for k in range(len(tiles)):
                    if tiles[k][j].getValue() == " " and tiles[k][j-1].getValue() != "*":
                        tiles[k][j].setValue(tiles[k][j-1].getValue())
                        tiles[k][j-1].setValue(" ")
        return tiles



while 1 == 1:
    select = menu()
    key = input("(W)Arriba, (A)Izquierda, (D)Derecha, (S)Abajo, (M)Modo, (G)Guardar, (F)Fin")
    if select == 1:
        print("Opcion 1")
        data = newGame()
        size = data[0]
        mode = data[1]
        tiles = data[2]
        newtiles = movement(tiles)
        board(size, mode, newtiles)
    else:
        print("Opcion 2 ")
