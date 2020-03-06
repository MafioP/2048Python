import tile
import random


def menu():
    print("***********************2048**********************")
    print("Emepezar nueva partida: 1")
    print("Empezar partida guardada: 2")
    print("Salir del juego: 3")
    select = int(input("Seleccione una opcion: "))
    return select


def board(size, blocks, mode, tiles):
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


def setGrid(size, blocks, mode):
    tiles = [[tile.Tile() for j in range(size)] for i in range(size)]
    tiles[randInt(size - 1)][randInt(size - 1)].setValue(1)
    count = 0
    for i in range(blocks):
        while count <= i:
            randX = randInt(size)
            randY = randInt(size)
            print("X:", randX, "Y:", randY)
            if tiles[randX][randY].getValue() == 0:
                tiles[randX][randY].setValue("*")
                count += 1
                print(count)
    return tiles


select = menu()
if select == 1:
    print("Opcion 1")
    size = int(input("Introduzca el tamaño del tablero"))
    blocks = int(input("Introduzca el numero de obstaculos"))
    mode = int(input("Introduzca el modo de juego"))
    tiles = setGrid(size, blocks, mode)
    board(size, blocks, mode, tiles)
else:
    print("Opcion 2 ")
