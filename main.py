import tile


def menu():
    print("***********************2048**********************")
    print("Emepezar nueva partida: 1")
    print("Empezar partida guardada: 2")
    print("Salir del juego: 3")
    select = int(input("Seleccione una opcion: "))
    if select == 1:
        print("Opcion 1")
        size = int(input("Introduzca el tamaño del tablero"))
        blocks = int(input("Introduzca el numero de obstaculos"))
        mode = int(input("Introduzca el modo de juego"))
        return board(size, blocks, mode)
    else:
        print("Opcion 2 ")
        return select

def board(size, blocks, mode):
    for i in range(size):
        print("+", end="")
        for j in range(size):
            for l in range(mode):
                print("-", end="")
            print("+", end="")
        print("")
        for k in range(size):
            print("|", end="")
            for m in range(mode):
                print(" ", end="")
        print("|")
    for j in range(size):
        print("+", end="")
        for k in range(mode):
            print("-", end="")
    print("+")



menu()

