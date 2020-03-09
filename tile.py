class Tile:
    def __init__(self):
        self.__value = 0

    def getValue(self):
        return self.__value

    def setValue(self, value):
        self.__value = value
        return None