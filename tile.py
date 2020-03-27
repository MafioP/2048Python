class Tile:
    def __init__(self):
        self.__value = " "
        self.__displayValue = " "

    def getValue(self):
        return self.__value

    def getDisplayValue(self):
        return self.__displayValue

    def setValue(self, value):
        self.__value = value

    def setMode(self, mode):
        mode1Dic = {1: "A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K"}
        if mode == 1 and self.__value != " " and self.__value != "*":        #modo letras
            self.__displayValue = mode1Dic[self.__value]
            print(self.__displayValue)
            return self.__displayValue
        if mode == 2 and self.__value != " " and self.__value != "*":
            self.__displayValue = self.__value
            return self.__displayValue
        if mode == 3 and self.__value != " " and self.__value != "*":
            self.__displayValue = 2**(int(self.__value))/2
            return self.__displayValue
        if mode == 4 and self.__value != " " and self.__value != "*":
            self.__displayValue = 2**(int(self.__value))
            return self.__displayValue
        else:
            return 0